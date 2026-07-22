# -*- coding: utf-8 -*-
"""Obliczanie zapotrzebowania kalorycznego pod redukcje masy ciala."""

ACTIVITY_FACTORS = {
    "siedzacy": 1.2,
    "lekko_aktywny": 1.375,
    "umiarkowanie_aktywny": 1.55,
    "bardzo_aktywny": 1.725,
    "sportowiec": 1.9,
}

ACTIVITY_LABELS = {
    "siedzacy": "Siedzący tryb życia (mało lub brak ćwiczeń)",
    "lekko_aktywny": "Lekko aktywny (1-3 treningi/tydzień)",
    "umiarkowanie_aktywny": "Umiarkowanie aktywny (3-5 treningów/tydzień)",
    "bardzo_aktywny": "Bardzo aktywny (6-7 treningów/tydzień)",
    "sportowiec": "Sportowiec (intensywny trening codziennie)",
}

# tempo utraty wagi w kg/tydzien -> deficyt kaloryczny dzienny (1 kg tkanki tluszczowej ~ 7700 kcal)
PACE_TO_DEFICIT = {
    0.25: 275,
    0.5: 550,
    0.75: 825,
}

MIN_CALORIES = {"kobieta": 1200, "mezczyzna": 1500}


def calculate_bmr(sex: str, weight_kg: float, height_cm: float, age: int) -> float:
    """Wzor Mifflin-St Jeor."""
    base = 10 * weight_kg + 6.25 * height_cm - 5 * age
    return base + 5 if sex == "mezczyzna" else base - 161


def calculate_target_calories(sex: str, weight_kg: float, height_cm: float, age: int,
                               activity: str, weekly_pace_kg: float) -> dict:
    bmr = calculate_bmr(sex, weight_kg, height_cm, age)
    tdee = bmr * ACTIVITY_FACTORS.get(activity, 1.2)
    deficit = PACE_TO_DEFICIT.get(weekly_pace_kg, 275)
    target = tdee - deficit
    min_cal = MIN_CALORIES.get(sex, 1200)
    target = max(target, min_cal)
    return {
        "bmr": round(bmr),
        "tdee": round(tdee),
        "deficit": deficit,
        "target_calories": round(target),
        "capped": target == min_cal and (tdee - deficit) < min_cal,
    }
