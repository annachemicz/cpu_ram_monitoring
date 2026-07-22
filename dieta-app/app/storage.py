# -*- coding: utf-8 -*-
"""Bardzo prosty magazyn danych oparty o pliki JSON (jeden uzytkownik, bez bazy danych)."""
import json
import os
from datetime import date

DATA_DIR = os.environ.get("DATA_DIR", os.path.join(os.path.dirname(os.path.dirname(__file__)), "data"))
PROFILE_PATH = os.path.join(DATA_DIR, "profile.json")
PLAN_PATH = os.path.join(DATA_DIR, "current_plan.json")
WEIGHT_LOG_PATH = os.path.join(DATA_DIR, "weight_log.json")

DEFAULT_PROFILE = {
    "sex": "kobieta",
    "weight_kg": 70,
    "height_cm": 165,
    "age": 30,
    "activity": "siedzacy",
    "weekly_pace_kg": 0.5,
    "goal_weight_kg": None,
    "allergies": [],
    "excluded_ingredients": [],
    "owned_shopping_items": [],
}


def _ensure_data_dir():
    os.makedirs(DATA_DIR, exist_ok=True)


def load_profile():
    _ensure_data_dir()
    if not os.path.exists(PROFILE_PATH):
        return dict(DEFAULT_PROFILE)
    with open(PROFILE_PATH, "r", encoding="utf-8") as f:
        profile = json.load(f)
    merged = dict(DEFAULT_PROFILE)
    merged.update(profile)
    merged.setdefault("owned_shopping_items", [])
    return merged


def save_profile(profile):
    _ensure_data_dir()
    profile.setdefault("owned_shopping_items", [])
    with open(PROFILE_PATH, "w", encoding="utf-8") as f:
        json.dump(profile, f, ensure_ascii=False, indent=2)


def has_profile():
    return os.path.exists(PROFILE_PATH)


def save_plan(plan_ids):
    """Zapisuje jadlospis jako liste id przepisow (kompaktowo), zeby odtworzyc go pozniej."""
    _ensure_data_dir()
    with open(PLAN_PATH, "w", encoding="utf-8") as f:
        json.dump(plan_ids, f, ensure_ascii=False, indent=2)


def load_plan_ids():
    if not os.path.exists(PLAN_PATH):
        return None
    with open(PLAN_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


# ---------------------------------------------------------------- postepy wagi

def load_weight_log():
    if not os.path.exists(WEIGHT_LOG_PATH):
        return []
    with open(WEIGHT_LOG_PATH, "r", encoding="utf-8") as f:
        log = json.load(f)
    return sorted(log, key=lambda e: e["date"])


def _save_weight_log(log):
    _ensure_data_dir()
    with open(WEIGHT_LOG_PATH, "w", encoding="utf-8") as f:
        json.dump(log, f, ensure_ascii=False, indent=2)


def record_weight(weight_kg, entry_date=None):
    """Dodaje/aktualizuje pomiar wagi dla danego dnia (domyslnie dzisiaj)."""
    entry_date = entry_date or date.today().isoformat()
    log = [e for e in load_weight_log() if e["date"] != entry_date]
    log.append({"date": entry_date, "weight_kg": weight_kg})
    log.sort(key=lambda e: e["date"])
    _save_weight_log(log)
    return log


def delete_weight_entry(entry_date):
    log = [e for e in load_weight_log() if e["date"] != entry_date]
    _save_weight_log(log)
    return log


def current_weight(fallback_weight_kg):
    log = load_weight_log()
    return log[-1]["weight_kg"] if log else fallback_weight_kg


def starting_weight(fallback_weight_kg):
    log = load_weight_log()
    return log[0]["weight_kg"] if log else fallback_weight_kg
