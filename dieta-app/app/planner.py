# -*- coding: utf-8 -*-
"""Generowanie wielodniowego jadlospisu dopasowanego do celu kalorycznego
oraz agregacja listy zakupow na podstawie wybranych przepisow.
"""
import random
from datetime import date, timedelta

from .recipes_data import RECIPES

WEEKDAY_NAMES = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota", "Niedziela"]
MEAL_SLOTS = ["sniadanie", "obiad", "kolacja"]
PLAN_LENGTH_OPTIONS = [7, 30, 90]
PLAN_LENGTH_LABELS = {7: "7 dni (1 tydzień)", 30: "30 dni (1 miesiąc)", 90: "90 dni (3 miesiące)"}


def weekday_name(a_date):
    return WEEKDAY_NAMES[a_date.weekday()]


def get_recipe_by_id(recipe_id):
    for r in RECIPES:
        if r["id"] == recipe_id:
            return r
    return None


def filter_by_allergies(recipes, allergies):
    """Zwraca przepisy, ktore NIE zawieraja zadnego z podanych alergenow."""
    if not allergies:
        return list(recipes)
    allergy_set = set(allergies)
    return [r for r in recipes if not (allergy_set & set(r.get("allergens", [])))]


_POLISH_DIACRITICS = str.maketrans("ąćęłńóśźż", "acelnoszz")


def normalize_text(text):
    return text.lower().translate(_POLISH_DIACRITICS).strip()


def filter_by_excluded_ingredients(recipes, excluded_ingredients):
    """Zwraca przepisy, ktore NIE zawieraja zadnego ze wskazanych skladnikow
    (dopasowanie tekstowe, np. wykluczenie konkretnego produktu spoza listy alergenow).
    """
    normalized_excluded = [normalize_text(e) for e in excluded_ingredients if e.strip()]
    if not normalized_excluded:
        return list(recipes)

    def recipe_is_ok(recipe):
        for ing in recipe["ingredients"]:
            ing_norm = normalize_text(ing["name"])
            for excluded in normalized_excluded:
                if excluded and (excluded in ing_norm or ing_norm in excluded):
                    return False
        return True

    return [r for r in recipes if recipe_is_ok(r)]


def get_available_recipes(recipes, allergies, excluded_ingredients):
    """Laczy filtrowanie po alergenach i po wykluczonych skladnikach."""
    recipes = filter_by_allergies(recipes, allergies)
    return filter_by_excluded_ingredients(recipes, excluded_ingredients)


def recipes_by_meal_type(recipes, meal_type):
    return [r for r in recipes if r["meal_type"] == meal_type]


def generate_plan(target_calories, allergies, excluded_ingredients=None, num_days=7, start_date=None):
    """Zwraca liste num_days dni, kazdy z przepisami sniadanie/obiad/kolacja(+przekaska)
    dobranymi tak, by suma kalorii byla jak najblizsza target_calories,
    z rotacja przepisow minimalizujaca powtorzenia w calym okresie.
    """
    available = get_available_recipes(RECIPES, allergies, excluded_ingredients or [])

    pools = {
        "sniadanie": recipes_by_meal_type(available, "sniadanie"),
        "obiad": recipes_by_meal_type(available, "obiad"),
        "kolacja": recipes_by_meal_type(available, "kolacja"),
        "przekaska": recipes_by_meal_type(available, "przekaska"),
    }

    missing_slots = [slot for slot in MEAL_SLOTS if not pools[slot]]
    if missing_slots:
        return {"error": "missing_recipes", "missing_slots": missing_slots}

    usage_count = {r["id"]: 0 for r in available}
    start_date = start_date or date.today()

    # baza kombinacji sniadanie/obiad/kolacja z roznica wzgledem celu (niezalezna od dnia) -
    # liczona raz, zeby nie przeliczac tego samego dla kazdego z wielu dni planu
    base_combos = []
    for b in pools["sniadanie"]:
        for l in pools["obiad"]:
            for d in pools["kolacja"]:
                total = b["calories"] + l["calories"] + d["calories"]
                base_combos.append((abs(total - target_calories), b, l, d, total))

    plan = []

    for day_index in range(num_days):
        scored = [
            (diff + (usage_count[b["id"]] + usage_count[l["id"]] + usage_count[d["id"]]) * 60, b, l, d, total)
            for diff, b, l, d, total in base_combos
        ]
        scored.sort(key=lambda c: c[0])
        top_candidates = scored[:5] if len(scored) >= 5 else scored
        _, breakfast, lunch, dinner, total_calories = random.choice(top_candidates)

        meals = {"sniadanie": breakfast, "obiad": lunch, "kolacja": dinner}
        remaining = target_calories - total_calories

        snack = None
        if remaining > 80 and pools["przekaska"]:
            snack_scored = sorted(
                pools["przekaska"],
                key=lambda s: abs(s["calories"] - remaining) + usage_count[s["id"]] * 60,
            )
            snack = snack_scored[0]
            meals["przekaska"] = snack
            total_calories += snack["calories"]

        for r in meals.values():
            usage_count[r["id"]] += 1

        day_date = start_date + timedelta(days=day_index)
        plan.append({
            "date": day_date.isoformat(),
            "day_name": weekday_name(day_date),
            "meals": meals,
            "total_calories": total_calories,
        })

    return {"error": None, "plan": plan}


def build_shopping_list(plan):
    """Agreguje skladniki ze wszystkich przepisow w jadlospisie.
    Zwraca slownik: kategoria -> lista {name, quantity, unit}.
    """
    aggregated = {}  # (name, unit) -> quantity
    categories = {}  # (name, unit) -> category

    for day in plan:
        for recipe in day["meals"].values():
            for ing in recipe["ingredients"]:
                key = (ing["name"], ing["unit"])
                aggregated[key] = aggregated.get(key, 0) + ing["quantity"]
                categories[key] = ing.get("category", "inne")

    grouped = {}
    for (name, unit), quantity in aggregated.items():
        category = categories[(name, unit)]
        grouped.setdefault(category, []).append({
            "name": name,
            "quantity": round(quantity, 2),
            "unit": unit,
        })

    for category in grouped:
        grouped[category].sort(key=lambda x: x["name"])

    return dict(sorted(grouped.items()))
