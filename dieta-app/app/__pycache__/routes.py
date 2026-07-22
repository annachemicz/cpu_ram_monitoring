# -*- coding: utf-8 -*-
from datetime import date

from flask import Blueprint, render_template, request, redirect, url_for, flash

from .calorie import calculate_target_calories, ACTIVITY_LABELS, PACE_TO_DEFICIT
from .planner import (
    generate_plan, build_shopping_list, get_recipe_by_id,
    get_available_recipes, normalize_text, weekday_name,
    PLAN_LENGTH_OPTIONS, PLAN_LENGTH_LABELS,
)
from .recipes_data import RECIPES, ALLERGEN_LABELS, METHOD_LABELS, MEAL_TYPE_LABELS
from . import storage

bp = Blueprint("main", __name__)


def _to_float(value, default):
    try:
        return float(value)
    except (TypeError, ValueError):
        return default


def _to_int(value, default):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _to_iso_date_or_none(value):
    try:
        date.fromisoformat(value)
        return value
    except (TypeError, ValueError):
        return None


def _rebuild_plan_from_entries(plan_entries):
    plan = []
    for entry in plan_entries:
        day_date = date.fromisoformat(entry["date"])
        meals = {}
        total_calories = 0
        for slot, recipe_id in entry["slots"].items():
            if recipe_id is None:
                continue
            recipe = get_recipe_by_id(recipe_id)
            if recipe is None:
                continue
            meals[slot] = recipe
            total_calories += recipe["calories"]
        plan.append({
            "date": entry["date"],
            "day_name": weekday_name(day_date),
            "meals": meals,
            "total_calories": total_calories,
        })
    return plan


def _plan_to_entries(plan):
    entries = []
    for day in plan:
        slots = {slot: recipe["id"] for slot, recipe in day["meals"].items()}
        entries.append({"date": day["date"], "slots": slots})
    return entries


def _target_calc(profile):
    weight = storage.current_weight(profile["weight_kg"])
    return calculate_target_calories(
        profile["sex"], weight, profile["height_cm"],
        profile["age"], profile["activity"], profile["weekly_pace_kg"],
    )


def _build_weight_chart(weight_log, width=640, height=220, padding=36):
    if len(weight_log) < 2:
        return None
    weights = [e["weight_kg"] for e in weight_log]
    min_w, max_w = min(weights), max(weights)
    if min_w == max_w:
        min_w -= 1
        max_w += 1
    n = len(weight_log)
    points = []
    for i, entry in enumerate(weight_log):
        x = padding + (width - 2 * padding) * (i / (n - 1))
        y = height - padding - (height - 2 * padding) * ((entry["weight_kg"] - min_w) / (max_w - min_w))
        points.append(f"{x:.1f},{y:.1f}")
    return {
        "points": " ".join(points),
        "width": width,
        "height": height,
        "min_weight": round(min_w, 1),
        "max_weight": round(max_w, 1),
    }


@bp.route("/")
def index():
    if not storage.has_profile():
        return redirect(url_for("main.profil"))
    return redirect(url_for("main.jadlospis"))


@bp.route("/profil", methods=["GET", "POST"])
def profil():
    if request.method == "POST":
        existing = storage.load_profile()
        goal_raw = request.form.get("goal_weight_kg", "").strip()
        weight_kg = _to_float(request.form.get("weight_kg"), existing.get("weight_kg", 70))
        profile = {
            "sex": request.form.get("sex", "kobieta"),
            "weight_kg": weight_kg,
            "height_cm": _to_float(request.form.get("height_cm"), existing.get("height_cm", 165)),
            "age": _to_int(request.form.get("age"), existing.get("age", 30)),
            "activity": request.form.get("activity", "siedzacy"),
            "weekly_pace_kg": _to_float(request.form.get("weekly_pace_kg"), 0.5),
            "goal_weight_kg": _to_float(goal_raw, None) if goal_raw else None,
            "allergies": request.form.getlist("allergies"),
            "excluded_ingredients": existing.get("excluded_ingredients", []),
        }
        storage.save_profile(profile)
        storage.record_weight(weight_kg)
        # usuwamy zapisany jadlospis, bo zmienil sie profil (cel kaloryczny / alergie / skladniki)
        storage.save_plan([])
        flash("Zapisano profil. Wygenerowano nowy cel kaloryczny.", "success")
        return redirect(url_for("main.jadlospis"))

    profile = storage.load_profile()
    calc = _target_calc(profile)
    return render_template(
        "profil.html",
        profile=profile,
        calc=calc,
        activity_labels=ACTIVITY_LABELS,
        pace_options=sorted(PACE_TO_DEFICIT.keys()),
        allergen_labels=ALLERGEN_LABELS,
    )


@bp.route("/profil/skladniki/dodaj", methods=["POST"])
def dodaj_wykluczony_skladnik():
    ingredient = request.form.get("ingredient", "").strip()
    if ingredient:
        profile = storage.load_profile()
        excluded = profile.get("excluded_ingredients", [])
        already_there = any(normalize_text(ingredient) == normalize_text(e) for e in excluded)
        if not already_there:
            excluded.append(ingredient)
            profile["excluded_ingredients"] = excluded
            storage.save_profile(profile)
            storage.save_plan([])
            flash(f"Dodano \"{ingredient}\" do wykluczonych składników.", "success")
    return redirect(url_for("main.profil"))


@bp.route("/profil/skladniki/usun", methods=["POST"])
def usun_wykluczony_skladnik():
    ingredient = request.form.get("ingredient", "")
    profile = storage.load_profile()
    excluded = [e for e in profile.get("excluded_ingredients", []) if e != ingredient]
    profile["excluded_ingredients"] = excluded
    storage.save_profile(profile)
    storage.save_plan([])
    return redirect(url_for("main.profil"))


@bp.route("/przepisy")
def przepisy():
    profile = storage.load_profile()
    method_filter = request.args.get("method", "wszystkie")
    recipes = get_available_recipes(RECIPES, profile["allergies"], profile.get("excluded_ingredients", []))
    if method_filter != "wszystkie":
        recipes = [r for r in recipes if r["method"] == method_filter]
    return render_template(
        "przepisy.html",
        recipes=recipes,
        method_filter=method_filter,
        method_labels=METHOD_LABELS,
        meal_type_labels=MEAL_TYPE_LABELS,
        allergen_labels=ALLERGEN_LABELS,
        profile=profile,
    )


@bp.route("/jadlospis")
def jadlospis():
    if not storage.has_profile():
        return redirect(url_for("main.profil"))

    profile = storage.load_profile()
    calc = _target_calc(profile)

    plan_entries = storage.load_plan_ids()
    if not plan_entries:
        result = generate_plan(calc["target_calories"], profile["allergies"], profile.get("excluded_ingredients", []),
                                num_days=7, start_date=date.today())
        if result["error"]:
            return render_template("jadlospis.html", error=result["error"],
                                    missing_slots=result.get("missing_slots"), calc=calc,
                                    meal_type_labels=MEAL_TYPE_LABELS, plan=None,
                                    plan_length_options=PLAN_LENGTH_OPTIONS, plan_length_labels=PLAN_LENGTH_LABELS,
                                    selected_days=7)
        plan = result["plan"]
        storage.save_plan(_plan_to_entries(plan))
    else:
        plan = _rebuild_plan_from_entries(plan_entries)

    return render_template(
        "jadlospis.html", plan=plan, calc=calc, error=None,
        meal_type_labels=MEAL_TYPE_LABELS, method_labels=METHOD_LABELS,
        plan_length_options=PLAN_LENGTH_OPTIONS, plan_length_labels=PLAN_LENGTH_LABELS,
        selected_days=len(plan),
    )


@bp.route("/jadlospis/generuj", methods=["POST"])
def generuj_jadlospis():
    profile = storage.load_profile()
    calc = _target_calc(profile)
    try:
        num_days = int(request.form.get("num_days", 7))
    except ValueError:
        num_days = 7
    if num_days not in PLAN_LENGTH_OPTIONS:
        num_days = 7

    result = generate_plan(calc["target_calories"], profile["allergies"], profile.get("excluded_ingredients", []),
                            num_days=num_days, start_date=date.today())
    if not result["error"]:
        storage.save_plan(_plan_to_entries(result["plan"]))
        flash(f"Wygenerowano nowy jadłospis na {num_days} dni.", "success")
    else:
        flash("Za mało przepisów (po wykluczeniu alergenów/składników), by ułożyć pełny jadłospis.", "error")
    return redirect(url_for("main.jadlospis"))


@bp.route("/lista-zakupow")
def lista_zakupow():
    if not storage.has_profile():
        return redirect(url_for("main.profil"))

    plan_entries = storage.load_plan_ids()
    if not plan_entries:
        flash("Najpierw wygeneruj jadłospis.", "error")
        return redirect(url_for("main.jadlospis"))

    plan = _rebuild_plan_from_entries(plan_entries)
    shopping_list = build_shopping_list(plan)
    return render_template("lista_zakupow.html", shopping_list=shopping_list, num_days=len(plan))


@bp.route("/postepy", methods=["GET"])
def postepy():
    if not storage.has_profile():
        return redirect(url_for("main.profil"))

    profile = storage.load_profile()
    weight_log = storage.load_weight_log()
    start_weight = storage.starting_weight(profile["weight_kg"])
    current = storage.current_weight(profile["weight_kg"])
    goal_weight = profile.get("goal_weight_kg")

    lost_so_far = round(start_weight - current, 1)
    remaining_to_goal = round(current - goal_weight, 1) if goal_weight else None

    progress_pct = None
    if goal_weight and start_weight != goal_weight:
        progress_pct = max(0, min(100, round((start_weight - current) / (start_weight - goal_weight) * 100)))

    chart = _build_weight_chart(weight_log)

    return render_template(
        "postepy.html",
        weight_log=list(reversed(weight_log)),
        start_weight=start_weight,
        current_weight=current,
        goal_weight=goal_weight,
        lost_so_far=lost_so_far,
        remaining_to_goal=remaining_to_goal,
        progress_pct=progress_pct,
        chart=chart,
    )


@bp.route("/postepy/dodaj", methods=["POST"])
def dodaj_pomiar_wagi():
    weight_kg = _to_float(request.form.get("weight_kg", "").strip(), None)
    entry_date = _to_iso_date_or_none(request.form.get("entry_date", "").strip())
    if weight_kg is not None:
        storage.record_weight(weight_kg, entry_date)
        profile = storage.load_profile()
        profile["weight_kg"] = storage.current_weight(profile["weight_kg"])
        storage.save_profile(profile)
        storage.save_plan([])
        flash("Zapisano pomiar wagi.", "success")
    else:
        flash("Podaj poprawną wagę (liczbę).", "error")
    return redirect(url_for("main.postepy"))


@bp.route("/postepy/usun", methods=["POST"])
def usun_pomiar_wagi():
    entry_date = request.form.get("entry_date", "")
    if entry_date:
        storage.delete_weight_entry(entry_date)
    return redirect(url_for("main.postepy"))
