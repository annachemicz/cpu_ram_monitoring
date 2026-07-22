# -*- coding: utf-8 -*-
"""Baza przepisow dietetycznych (dane statyczne, wbudowane w aplikacje).

Kazdy przepis ma:
- method: "air_fryer" | "lidlomix" | "tradycyjne"
- meal_type: "sniadanie" | "obiad" | "kolacja" | "przekaska"
- calories / protein_g / fat_g / carbs_g: wartosci na 1 porcje
- allergens: lista alergenow wystepujacych w przepisie
- ingredients: lista skladnikow z iloscia (na 1 porcje) i kategoria (do listy zakupow)

Dostepne alergeny (zgodnie z lista alergenow UE, ograniczone do praktycznych w domowej kuchni):
gluten, laktoza, jaja, orzechy, orzeszki_ziemne, ryby, skorupiaki, soja, seler, gorczyca, sezam
"""

RECIPES = [
    # ---------------------------------------------------------------- SNIADANIA
    {
        "id": 1, "name": "Owsianka z owocami i orzechami", "method": "tradycyjne", "meal_type": "sniadanie",
        "servings": 1, "calories": 360, "protein_g": 12, "fat_g": 11, "carbs_g": 54,
        "allergens": ["gluten", "orzechy", "laktoza"],
        "ingredients": [
            {"name": "płatki owsiane", "quantity": 50, "unit": "g", "category": "produkty sypkie"},
            {"name": "mleko", "quantity": 200, "unit": "ml", "category": "nabial"},
            {"name": "banan", "quantity": 1, "unit": "szt", "category": "owoce"},
            {"name": "orzechy wloskie", "quantity": 15, "unit": "g", "category": "bakalie"},
            {"name": "miod", "quantity": 1, "unit": "łyżeczka", "category": "inne"},
        ],
        "instructions": "1. Zagotuj mleko. 2. Wsyp platki owsiane i gotuj 3-4 min mieszajac. "
                        "3. Przelej do miski, dodaj pokrojonego banana, orzechy i polej miodem.",
    },
    {
        "id": 2, "name": "Jajecznica na maśle z pomidorem", "method": "tradycyjne", "meal_type": "sniadanie",
        "servings": 1, "calories": 310, "protein_g": 20, "fat_g": 24, "carbs_g": 5,
        "allergens": ["jaja", "laktoza"],
        "ingredients": [
            {"name": "jajko", "quantity": 3, "unit": "szt", "category": "nabial"},
            {"name": "masło", "quantity": 10, "unit": "g", "category": "nabial"},
            {"name": "pomidor", "quantity": 1, "unit": "szt", "category": "warzywa"},
            {"name": "szczypiorek", "quantity": 1, "unit": "pęczek", "category": "warzywa"},
        ],
        "instructions": "1. Roztop maslo na patelni. 2. Wbij jajka, mieszaj na wolnym ogniu. "
                        "3. Podawaj z pokrojonym pomidorem i szczypiorkiem.",
    },
    {
        "id": 3, "name": "Jogurt naturalny z granola i owocami", "method": "tradycyjne", "meal_type": "sniadanie",
        "servings": 1, "calories": 320, "protein_g": 15, "fat_g": 9, "carbs_g": 46,
        "allergens": ["laktoza", "gluten", "orzechy"],
        "ingredients": [
            {"name": "jogurt naturalny", "quantity": 200, "unit": "g", "category": "nabial"},
            {"name": "granola", "quantity": 40, "unit": "g", "category": "produkty sypkie"},
            {"name": "borowki", "quantity": 80, "unit": "g", "category": "owoce"},
        ],
        "instructions": "1. Jogurt przelej do miski. 2. Dodaj granole i borowki. Wymieszaj przed jedzeniem.",
    },
    {
        "id": 4, "name": "Kanapki z pastą jajeczną", "method": "tradycyjne", "meal_type": "sniadanie",
        "servings": 1, "calories": 340, "protein_g": 16, "fat_g": 16, "carbs_g": 32,
        "allergens": ["jaja", "gluten", "gorczyca"],
        "ingredients": [
            {"name": "chleb razowy", "quantity": 60, "unit": "g", "category": "pieczywo"},
            {"name": "jajko", "quantity": 2, "unit": "szt", "category": "nabial"},
            {"name": "majonez", "quantity": 15, "unit": "g", "category": "inne"},
            {"name": "szczypiorek", "quantity": 1, "unit": "łyżka", "category": "warzywa"},
        ],
        "instructions": "1. Ugotuj jajka na twardo, ostudz i zetrzyj. 2. Wymieszaj z majonezem i szczypiorkiem. "
                        "3. Posmaruj kromki chleba.",
    },
    {
        "id": 5, "name": "Omlet z warzywami z air fryera", "method": "air_fryer", "meal_type": "sniadanie",
        "servings": 1, "calories": 280, "protein_g": 19, "fat_g": 17, "carbs_g": 10,
        "allergens": ["jaja", "laktoza"],
        "ingredients": [
            {"name": "jajko", "quantity": 3, "unit": "szt", "category": "nabial"},
            {"name": "papryka", "quantity": 0.5, "unit": "szt", "category": "warzywa"},
            {"name": "cebula", "quantity": 0.25, "unit": "szt", "category": "warzywa"},
            {"name": "ser żółty", "quantity": 20, "unit": "g", "category": "nabial"},
        ],
        "instructions": "1. Roztrzep jajka z posiekanymi warzywami i serem. 2. Przelej do naczynia do air fryera. "
                        "3. Piecz w 170°C ok. 10-12 min.",
    },
    {
        "id": 6, "name": "Placuszki bananowe z air fryera", "method": "air_fryer", "meal_type": "sniadanie",
        "servings": 1, "calories": 300, "protein_g": 10, "fat_g": 7, "carbs_g": 50,
        "allergens": ["jaja", "gluten", "laktoza"],
        "ingredients": [
            {"name": "banan", "quantity": 1, "unit": "szt", "category": "owoce"},
            {"name": "jajko", "quantity": 1, "unit": "szt", "category": "nabial"},
            {"name": "maka owsiana", "quantity": 40, "unit": "g", "category": "produkty sypkie"},
            {"name": "jogurt naturalny", "quantity": 30, "unit": "g", "category": "nabial"},
        ],
        "instructions": "1. Zmiksuj wszystkie skladniki na gladkie ciasto. 2. Uformuj placuszki na papierze do pieczenia. "
                        "3. Piecz w air fryerze 180°C ok. 8 min, przewracajac w polowie.",
    },
    {
        "id": 7, "name": "Twarog z rzodkiewka i szczypiorkiem", "method": "tradycyjne", "meal_type": "sniadanie",
        "servings": 1, "calories": 250, "protein_g": 24, "fat_g": 9, "carbs_g": 14,
        "allergens": ["laktoza"],
        "ingredients": [
            {"name": "twarog polttusty", "quantity": 150, "unit": "g", "category": "nabial"},
            {"name": "rzodkiewka", "quantity": 5, "unit": "szt", "category": "warzywa"},
            {"name": "szczypiorek", "quantity": 1, "unit": "łyżka", "category": "warzywa"},
            {"name": "jogurt naturalny", "quantity": 30, "unit": "g", "category": "nabial"},
        ],
        "instructions": "1. Rozgnieć twarog z jogurtem. 2. Dodaj posiekaną rzodkiewkę i szczypiorek, wymieszaj.",
    },
    {
        "id": 8, "name": "Smoothie owocowo-szpinakowe", "method": "tradycyjne", "meal_type": "sniadanie",
        "servings": 1, "calories": 260, "protein_g": 9, "fat_g": 4, "carbs_g": 48,
        "allergens": ["laktoza"],
        "ingredients": [
            {"name": "szpinak swiezy", "quantity": 30, "unit": "g", "category": "warzywa"},
            {"name": "banan", "quantity": 1, "unit": "szt", "category": "owoce"},
            {"name": "mleko", "quantity": 200, "unit": "ml", "category": "nabial"},
            {"name": "truskawki mrozone", "quantity": 80, "unit": "g", "category": "owoce"},
        ],
        "instructions": "1. Wszystkie skladniki zmiksuj na gladko. 2. Podawaj od razu.",
    },
    {
        "id": 9, "name": "Chałka francuska z Lidlomixa", "method": "lidlomix", "meal_type": "sniadanie",
        "servings": 1, "calories": 350, "protein_g": 12, "fat_g": 14, "carbs_g": 45,
        "allergens": ["jaja", "gluten", "laktoza"],
        "ingredients": [
            {"name": "chalka", "quantity": 60, "unit": "g", "category": "pieczywo"},
            {"name": "jajko", "quantity": 1, "unit": "szt", "category": "nabial"},
            {"name": "mleko", "quantity": 50, "unit": "ml", "category": "nabial"},
            {"name": "cynamon", "quantity": 1, "unit": "szczypta", "category": "przyprawy"},
        ],
        "instructions": "1. Umieść jajko, mleko i cynamon w naczyniu Lidlomixa, wymieszaj (10 sek/pr.3). "
                        "2. Namocz kromki chałki, podsmaż na patelni po 2 min z każdej strony.",
    },
    {
        "id": 10, "name": "Budyń jaglany z owocami", "method": "lidlomix", "meal_type": "sniadanie",
        "servings": 1, "calories": 300, "protein_g": 9, "fat_g": 6, "carbs_g": 54,
        "allergens": ["laktoza"],
        "ingredients": [
            {"name": "kasza jaglana", "quantity": 50, "unit": "g", "category": "produkty sypkie"},
            {"name": "mleko", "quantity": 200, "unit": "ml", "category": "nabial"},
            {"name": "jabłko", "quantity": 1, "unit": "szt", "category": "owoce"},
            {"name": "cynamon", "quantity": 1, "unit": "szczypta", "category": "przyprawy"},
        ],
        "instructions": "1. Ugotuj kaszę jaglaną w programie gotowania na parze/zupa (100°C, 20 min). "
                        "2. Dodaj mleko, starte jabłko i cynamon, wymieszaj programem 2 min/pr.2.",
    },
    {
        "id": 11, "name": "Serek wiejski z ogórkiem i pomidorem", "method": "tradycyjne", "meal_type": "sniadanie",
        "servings": 1, "calories": 230, "protein_g": 18, "fat_g": 8, "carbs_g": 18,
        "allergens": ["laktoza"],
        "ingredients": [
            {"name": "serek wiejski", "quantity": 200, "unit": "g", "category": "nabial"},
            {"name": "ogorek", "quantity": 0.5, "unit": "szt", "category": "warzywa"},
            {"name": "pomidor", "quantity": 1, "unit": "szt", "category": "warzywa"},
        ],
        "instructions": "1. Pokrój warzywa w kostkę. 2. Wymieszaj z serkiem wiejskim.",
    },
    {
        "id": 12, "name": "Pasta z awokado na grzance", "method": "air_fryer", "meal_type": "sniadanie",
        "servings": 1, "calories": 330, "protein_g": 9, "fat_g": 20, "carbs_g": 30,
        "allergens": ["gluten"],
        "ingredients": [
            {"name": "chleb razowy", "quantity": 50, "unit": "g", "category": "pieczywo"},
            {"name": "awokado", "quantity": 0.5, "unit": "szt", "category": "warzywa"},
            {"name": "cytryna", "quantity": 1, "unit": "łyżeczka soku", "category": "owoce"},
            {"name": "chili płatki", "quantity": 1, "unit": "szczypta", "category": "przyprawy"},
        ],
        "instructions": "1. Chleb przypiecz w air fryerze 180°C przez 3 min. 2. Rozgnieć awokado z sokiem z cytryny "
                        "i chili. 3. Posmaruj grzankę.",
    },

    # ---------------------------------------------------------------- OBIADY
    {
        "id": 20, "name": "Pierś z kurczaka z air fryera z brokułem", "method": "air_fryer", "meal_type": "obiad",
        "servings": 1, "calories": 420, "protein_g": 45, "fat_g": 14, "carbs_g": 28,
        "allergens": [],
        "ingredients": [
            {"name": "pierś z kurczaka", "quantity": 180, "unit": "g", "category": "mięso"},
            {"name": "brokuł", "quantity": 200, "unit": "g", "category": "warzywa"},
            {"name": "ziemniaki", "quantity": 150, "unit": "g", "category": "warzywa"},
            {"name": "oliwa z oliwek", "quantity": 10, "unit": "ml", "category": "inne"},
        ],
        "instructions": "1. Kurczaka przypraw i skrop oliwą. 2. Piecz w air fryerze 200°C 15 min. "
                        "3. Brokuł i ziemniaki piecz osobno 180°C 12 min.",
    },
    {
        "id": 21, "name": "Łosoś z air fryera z warzywami", "method": "air_fryer", "meal_type": "obiad",
        "servings": 1, "calories": 460, "protein_g": 38, "fat_g": 26, "carbs_g": 18,
        "allergens": ["ryby"],
        "ingredients": [
            {"name": "filet z łososia", "quantity": 150, "unit": "g", "category": "ryby"},
            {"name": "cukinia", "quantity": 150, "unit": "g", "category": "warzywa"},
            {"name": "papryka", "quantity": 100, "unit": "g", "category": "warzywa"},
            {"name": "cytryna", "quantity": 0.5, "unit": "szt", "category": "owoce"},
        ],
        "instructions": "1. Łososia przypraw solą, pieprzem i cytryną. 2. Piecz w air fryerze 200°C 10 min. "
                        "3. Warzywa piecz razem, skropione oliwą, 180°C 10 min.",
    },
    {
        "id": 22, "name": "Gulasz wołowy z Lidlomixa", "method": "lidlomix", "meal_type": "obiad",
        "servings": 1, "calories": 480, "protein_g": 36, "fat_g": 20, "carbs_g": 36,
        "allergens": ["seler"],
        "ingredients": [
            {"name": "wołowina gulaszowa", "quantity": 150, "unit": "g", "category": "mięso"},
            {"name": "marchew", "quantity": 80, "unit": "g", "category": "warzywa"},
            {"name": "cebula", "quantity": 50, "unit": "g", "category": "warzywa"},
            {"name": "seler korzeniowy", "quantity": 30, "unit": "g", "category": "warzywa"},
            {"name": "kasza gryczana", "quantity": 60, "unit": "g", "category": "produkty sypkie"},
        ],
        "instructions": "1. Warzywa posiekaj programem (5 sek/pr.5). 2. Podsmaż z mięsem (Varoma/120°C, 10 min). "
                        "3. Duś programem gotowania 90°C przez 40 min. Podawaj z kaszą.",
    },
    {
        "id": 23, "name": "Krem z dyni z Lidlomixa", "method": "lidlomix", "meal_type": "obiad",
        "servings": 1, "calories": 260, "protein_g": 7, "fat_g": 9, "carbs_g": 38,
        "allergens": ["laktoza"],
        "ingredients": [
            {"name": "dynia", "quantity": 250, "unit": "g", "category": "warzywa"},
            {"name": "marchew", "quantity": 50, "unit": "g", "category": "warzywa"},
            {"name": "bulion warzywny", "quantity": 200, "unit": "ml", "category": "inne"},
            {"name": "śmietanka 12%", "quantity": 30, "unit": "ml", "category": "nabial"},
        ],
        "instructions": "1. Warzywa i bulion gotuj programem zupa (100°C, 20 min). 2. Zmiksuj (30 sek/pr.8). "
                        "3. Dodaj śmietankę i wymieszaj.",
    },
    {
        "id": 24, "name": "Spaghetti bolognese", "method": "tradycyjne", "meal_type": "obiad",
        "servings": 1, "calories": 520, "protein_g": 28, "fat_g": 16, "carbs_g": 66,
        "allergens": ["gluten", "seler"],
        "ingredients": [
            {"name": "makaron spaghetti", "quantity": 80, "unit": "g", "category": "produkty sypkie"},
            {"name": "mięso mielone wołowe", "quantity": 120, "unit": "g", "category": "mięso"},
            {"name": "passata pomidorowa", "quantity": 150, "unit": "g", "category": "inne"},
            {"name": "cebula", "quantity": 40, "unit": "g", "category": "warzywa"},
            {"name": "seler naciowy", "quantity": 20, "unit": "g", "category": "warzywa"},
        ],
        "instructions": "1. Ugotuj makaron. 2. Podsmaż mięso z cebulą i selerem, dodaj passatę, duś 15 min. "
                        "3. Połącz z makaronem.",
    },
    {
        "id": 25, "name": "Indyk duszony z warzywami", "method": "tradycyjne", "meal_type": "obiad",
        "servings": 1, "calories": 400, "protein_g": 40, "fat_g": 12, "carbs_g": 30,
        "allergens": [],
        "ingredients": [
            {"name": "pierś z indyka", "quantity": 170, "unit": "g", "category": "mięso"},
            {"name": "papryka", "quantity": 100, "unit": "g", "category": "warzywa"},
            {"name": "cukinia", "quantity": 100, "unit": "g", "category": "warzywa"},
            {"name": "ryż", "quantity": 60, "unit": "g", "category": "produkty sypkie"},
        ],
        "instructions": "1. Pokrój indyka w kostkę, podsmaż. 2. Dodaj warzywa, duś 15 min. 3. Podawaj z ryżem.",
    },
    {
        "id": 26, "name": "Kotlety z indyka z air fryera", "method": "air_fryer", "meal_type": "obiad",
        "servings": 1, "calories": 410, "protein_g": 38, "fat_g": 15, "carbs_g": 28,
        "allergens": ["jaja", "gluten"],
        "ingredients": [
            {"name": "mięso mielone z indyka", "quantity": 150, "unit": "g", "category": "mięso"},
            {"name": "jajko", "quantity": 1, "unit": "szt", "category": "nabial"},
            {"name": "bułka tarta", "quantity": 20, "unit": "g", "category": "produkty sypkie"},
            {"name": "ziemniaki", "quantity": 150, "unit": "g", "category": "warzywa"},
        ],
        "instructions": "1. Wymieszaj mięso z jajkiem i bułką tartą, uformuj kotlety. "
                        "2. Piecz w air fryerze 190°C 12 min. 3. Ziemniaki piecz osobno 180°C 15 min.",
    },
    {
        "id": 27, "name": "Ryż z warzywami i krewetkami z Lidlomixa", "method": "lidlomix", "meal_type": "obiad",
        "servings": 1, "calories": 420, "protein_g": 26, "fat_g": 10, "carbs_g": 58,
        "allergens": ["skorupiaki", "soja", "gluten"],
        "ingredients": [
            {"name": "ryż", "quantity": 70, "unit": "g", "category": "produkty sypkie"},
            {"name": "krewetki", "quantity": 120, "unit": "g", "category": "ryby"},
            {"name": "marchew", "quantity": 60, "unit": "g", "category": "warzywa"},
            {"name": "groszek", "quantity": 50, "unit": "g", "category": "warzywa"},
            {"name": "sos sojowy", "quantity": 10, "unit": "ml", "category": "inne"},
        ],
        "instructions": "1. Ugotuj ryż programem gotowanie na parze. 2. Podsmaż krewetki i warzywa (Varoma 10 min). "
                        "3. Połącz wszystko, dodaj sos sojowy.",
    },
    {
        "id": 28, "name": "Pieczony dorsz z ziemniakami", "method": "air_fryer", "meal_type": "obiad",
        "servings": 1, "calories": 380, "protein_g": 34, "fat_g": 10, "carbs_g": 36,
        "allergens": ["ryby"],
        "ingredients": [
            {"name": "filet z dorsza", "quantity": 180, "unit": "g", "category": "ryby"},
            {"name": "ziemniaki", "quantity": 200, "unit": "g", "category": "warzywa"},
            {"name": "koperek", "quantity": 1, "unit": "łyżka", "category": "warzywa"},
        ],
        "instructions": "1. Dorsza przypraw i skrop oliwą. 2. Piecz w air fryerze 190°C 10 min. "
                        "3. Ziemniaki piecz osobno 180°C 15 min, posyp koperkiem.",
    },
    {
        "id": 29, "name": "Chili con carne", "method": "tradycyjne", "meal_type": "obiad",
        "servings": 1, "calories": 450, "protein_g": 32, "fat_g": 14, "carbs_g": 48,
        "allergens": [],
        "ingredients": [
            {"name": "mięso mielone wołowe", "quantity": 120, "unit": "g", "category": "mięso"},
            {"name": "fasola czerwona", "quantity": 100, "unit": "g", "category": "warzywa"},
            {"name": "kukurydza", "quantity": 50, "unit": "g", "category": "warzywa"},
            {"name": "passata pomidorowa", "quantity": 150, "unit": "g", "category": "inne"},
            {"name": "cebula", "quantity": 40, "unit": "g", "category": "warzywa"},
        ],
        "instructions": "1. Podsmaż mięso z cebulą. 2. Dodaj fasolę, kukurydzę i passatę. "
                        "3. Duś 20 min na małym ogniu.",
    },
    {
        "id": 30, "name": "Curry warzywne z ciecierzycą z Lidlomixa", "method": "lidlomix", "meal_type": "obiad",
        "servings": 1, "calories": 400, "protein_g": 16, "fat_g": 14, "carbs_g": 52,
        "allergens": [],
        "ingredients": [
            {"name": "ciecierzyca", "quantity": 150, "unit": "g", "category": "warzywa"},
            {"name": "mleko kokosowe", "quantity": 100, "unit": "ml", "category": "inne"},
            {"name": "papryka", "quantity": 80, "unit": "g", "category": "warzywa"},
            {"name": "curry przyprawa", "quantity": 1, "unit": "łyżeczka", "category": "przyprawy"},
            {"name": "ryż", "quantity": 60, "unit": "g", "category": "produkty sypkie"},
        ],
        "instructions": "1. Warzywa i ciecierzycę duś z curry i mlekiem kokosowym programem 90°C 20 min. "
                        "2. Podawaj z ryżem ugotowanym programem gotowanie na parze.",
    },
    {
        "id": 31, "name": "Klopsiki w sosie pomidorowym z air fryera", "method": "air_fryer", "meal_type": "obiad",
        "servings": 1, "calories": 440, "protein_g": 34, "fat_g": 18, "carbs_g": 34,
        "allergens": ["jaja", "gluten"],
        "ingredients": [
            {"name": "mięso mielone wieprzowo-wołowe", "quantity": 150, "unit": "g", "category": "mięso"},
            {"name": "jajko", "quantity": 1, "unit": "szt", "category": "nabial"},
            {"name": "bułka tarta", "quantity": 15, "unit": "g", "category": "produkty sypkie"},
            {"name": "passata pomidorowa", "quantity": 120, "unit": "g", "category": "inne"},
            {"name": "kasza gryczana", "quantity": 60, "unit": "g", "category": "produkty sypkie"},
        ],
        "instructions": "1. Uformuj klopsiki, piecz w air fryerze 190°C 10 min. "
                        "2. Podgrzej passatę, wrzuć klopsiki na 5 min. 3. Podawaj z kaszą.",
    },
    {
        "id": 32, "name": "Pieczona pierś kaczki z warzywami", "method": "air_fryer", "meal_type": "obiad",
        "servings": 1, "calories": 470, "protein_g": 36, "fat_g": 26, "carbs_g": 20,
        "allergens": [],
        "ingredients": [
            {"name": "pierś z kaczki", "quantity": 150, "unit": "g", "category": "mięso"},
            {"name": "buraki", "quantity": 150, "unit": "g", "category": "warzywa"},
            {"name": "jabłko", "quantity": 0.5, "unit": "szt", "category": "owoce"},
        ],
        "instructions": "1. Kaczkę natnij ze skóry, przypraw. 2. Piecz w air fryerze 180°C 15 min. "
                        "3. Buraki i jabłko piecz osobno 12 min.",
    },
    {
        "id": 33, "name": "Zupa krem z brokuła", "method": "lidlomix", "meal_type": "obiad",
        "servings": 1, "calories": 240, "protein_g": 10, "fat_g": 8, "carbs_g": 30,
        "allergens": ["laktoza"],
        "ingredients": [
            {"name": "brokuł", "quantity": 250, "unit": "g", "category": "warzywa"},
            {"name": "bulion warzywny", "quantity": 200, "unit": "ml", "category": "inne"},
            {"name": "ser topiony", "quantity": 30, "unit": "g", "category": "nabial"},
        ],
        "instructions": "1. Gotuj brokuł z bulionem programem zupa (100°C, 20 min). "
                        "2. Dodaj ser, zmiksuj programem 30 sek/pr.8.",
    },
    {
        "id": 34, "name": "Sałatka z tuńczykiem i fasolą", "method": "tradycyjne", "meal_type": "obiad",
        "servings": 1, "calories": 380, "protein_g": 30, "fat_g": 16, "carbs_g": 26,
        "allergens": ["ryby", "jaja", "gorczyca"],
        "ingredients": [
            {"name": "tuńczyk w sosie własnym", "quantity": 120, "unit": "g", "category": "ryby"},
            {"name": "fasola biała", "quantity": 100, "unit": "g", "category": "warzywa"},
            {"name": "jajko", "quantity": 1, "unit": "szt", "category": "nabial"},
            {"name": "pomidor", "quantity": 1, "unit": "szt", "category": "warzywa"},
            {"name": "musztarda", "quantity": 1, "unit": "łyżeczka", "category": "inne"},
        ],
        "instructions": "1. Ugotuj jajko na twardo. 2. Wymieszaj tuńczyka, fasolę, pokrojone jajko i pomidora. "
                        "3. Dopraw musztardą.",
    },
    {
        "id": 35, "name": "Pieczone udka kurczaka z air fryera", "method": "air_fryer", "meal_type": "obiad",
        "servings": 1, "calories": 450, "protein_g": 38, "fat_g": 24, "carbs_g": 20,
        "allergens": [],
        "ingredients": [
            {"name": "udka z kurczaka", "quantity": 200, "unit": "g", "category": "mięso"},
            {"name": "marchew", "quantity": 100, "unit": "g", "category": "warzywa"},
            {"name": "ziemniaki", "quantity": 150, "unit": "g", "category": "warzywa"},
        ],
        "instructions": "1. Udka przypraw. 2. Piecz w air fryerze 190°C 20 min. "
                        "3. Marchew i ziemniaki piecz osobno 180°C 15 min.",
    },

    # ---------------------------------------------------------------- KOLACJE
    {
        "id": 40, "name": "Sałatka grecka z fetą", "method": "tradycyjne", "meal_type": "kolacja",
        "servings": 1, "calories": 320, "protein_g": 12, "fat_g": 24, "carbs_g": 14,
        "allergens": ["laktoza"],
        "ingredients": [
            {"name": "ogorek", "quantity": 100, "unit": "g", "category": "warzywa"},
            {"name": "pomidor", "quantity": 100, "unit": "g", "category": "warzywa"},
            {"name": "papryka", "quantity": 50, "unit": "g", "category": "warzywa"},
            {"name": "ser feta", "quantity": 60, "unit": "g", "category": "nabial"},
            {"name": "oliwki", "quantity": 30, "unit": "g", "category": "inne"},
            {"name": "oliwa z oliwek", "quantity": 10, "unit": "ml", "category": "inne"},
        ],
        "instructions": "1. Warzywa pokrój w kostkę. 2. Dodaj fetę i oliwki. 3. Skrop oliwą.",
    },
    {
        "id": 41, "name": "Krewetki z air fryera z czosnkiem", "method": "air_fryer", "meal_type": "kolacja",
        "servings": 1, "calories": 260, "protein_g": 28, "fat_g": 12, "carbs_g": 8,
        "allergens": ["skorupiaki"],
        "ingredients": [
            {"name": "krewetki", "quantity": 180, "unit": "g", "category": "ryby"},
            {"name": "czosnek", "quantity": 2, "unit": "ząbki", "category": "warzywa"},
            {"name": "cytryna", "quantity": 0.5, "unit": "szt", "category": "owoce"},
        ],
        "instructions": "1. Krewetki wymieszaj z czosnkiem i oliwą. 2. Piecz w air fryerze 200°C 6-8 min. "
                        "3. Skrop cytryną.",
    },
    {
        "id": 42, "name": "Twarożek ze szczypiorkiem i rzodkiewką", "method": "tradycyjne", "meal_type": "kolacja",
        "servings": 1, "calories": 240, "protein_g": 22, "fat_g": 8, "carbs_g": 16,
        "allergens": ["laktoza", "gluten"],
        "ingredients": [
            {"name": "twarog polttusty", "quantity": 150, "unit": "g", "category": "nabial"},
            {"name": "rzodkiewka", "quantity": 5, "unit": "szt", "category": "warzywa"},
            {"name": "chleb razowy", "quantity": 30, "unit": "g", "category": "pieczywo"},
        ],
        "instructions": "1. Rozgnieć twaróg. 2. Dodaj posiekaną rzodkiewkę. 3. Podawaj z kromką chleba.",
    },
    {
        "id": 43, "name": "Zupa krem z pomidorów z Lidlomixa", "method": "lidlomix", "meal_type": "kolacja",
        "servings": 1, "calories": 220, "protein_g": 7, "fat_g": 9, "carbs_g": 26,
        "allergens": ["laktoza"],
        "ingredients": [
            {"name": "pomidory", "quantity": 300, "unit": "g", "category": "warzywa"},
            {"name": "cebula", "quantity": 40, "unit": "g", "category": "warzywa"},
            {"name": "śmietanka 12%", "quantity": 30, "unit": "ml", "category": "nabial"},
            {"name": "bazylia", "quantity": 1, "unit": "łyżka", "category": "przyprawy"},
        ],
        "instructions": "1. Podsmaż cebulę programem (5 min/120°C). 2. Dodaj pomidory, gotuj 15 min. "
                        "3. Zmiksuj, dodaj śmietankę i bazylię.",
    },
    {
        "id": 44, "name": "Pieczony camembert z żurawiną", "method": "air_fryer", "meal_type": "kolacja",
        "servings": 1, "calories": 380, "protein_g": 18, "fat_g": 26, "carbs_g": 18,
        "allergens": ["laktoza"],
        "ingredients": [
            {"name": "camembert", "quantity": 100, "unit": "g", "category": "nabial"},
            {"name": "żurawina suszona", "quantity": 20, "unit": "g", "category": "bakalie"},
            {"name": "pieczywo chrupkie", "quantity": 30, "unit": "g", "category": "pieczywo"},
        ],
        "instructions": "1. Camembert piecz w air fryerze 180°C 6-8 min. 2. Podawaj z żurawiną i pieczywem.",
    },
    {
        "id": 45, "name": "Kanapki z pastą z awokado i jajkiem", "method": "tradycyjne", "meal_type": "kolacja",
        "servings": 1, "calories": 350, "protein_g": 14, "fat_g": 22, "carbs_g": 26,
        "allergens": ["jaja", "gluten"],
        "ingredients": [
            {"name": "chleb razowy", "quantity": 50, "unit": "g", "category": "pieczywo"},
            {"name": "awokado", "quantity": 0.5, "unit": "szt", "category": "warzywa"},
            {"name": "jajko", "quantity": 1, "unit": "szt", "category": "nabial"},
        ],
        "instructions": "1. Ugotuj jajko na twardo. 2. Rozgnieć awokado na chlebie. 3. Ułóż plastry jajka na wierzchu.",
    },
    {
        "id": 46, "name": "Filet z indyka z air fryera z surówką", "method": "air_fryer", "meal_type": "kolacja",
        "servings": 1, "calories": 340, "protein_g": 34, "fat_g": 12, "carbs_g": 20,
        "allergens": [],
        "ingredients": [
            {"name": "pierś z indyka", "quantity": 150, "unit": "g", "category": "mięso"},
            {"name": "kapusta biała", "quantity": 100, "unit": "g", "category": "warzywa"},
            {"name": "marchew", "quantity": 50, "unit": "g", "category": "warzywa"},
        ],
        "instructions": "1. Indyka piecz w air fryerze 190°C 12 min. 2. Kapustę i marchew zetrzyj na surówkę.",
    },
    {
        "id": 47, "name": "Hummus z warzywami", "method": "lidlomix", "meal_type": "kolacja",
        "servings": 1, "calories": 300, "protein_g": 11, "fat_g": 16, "carbs_g": 28,
        "allergens": ["sezam"],
        "ingredients": [
            {"name": "ciecierzyca", "quantity": 150, "unit": "g", "category": "warzywa"},
            {"name": "tahini", "quantity": 20, "unit": "g", "category": "inne"},
            {"name": "cytryna", "quantity": 0.5, "unit": "szt", "category": "owoce"},
            {"name": "marchew", "quantity": 80, "unit": "g", "category": "warzywa"},
            {"name": "ogorek", "quantity": 80, "unit": "g", "category": "warzywa"},
        ],
        "instructions": "1. Zmiksuj ciecierzycę z tahini i sokiem z cytryny (30 sek/pr.8). "
                        "2. Podawaj z warzywami pokrojonymi w słupki.",
    },
    {
        "id": 48, "name": "Sałatka z kurczakiem z air fryera", "method": "air_fryer", "meal_type": "kolacja",
        "servings": 1, "calories": 360, "protein_g": 36, "fat_g": 14, "carbs_g": 18,
        "allergens": ["gorczyca"],
        "ingredients": [
            {"name": "pierś z kurczaka", "quantity": 150, "unit": "g", "category": "mięso"},
            {"name": "sałata", "quantity": 60, "unit": "g", "category": "warzywa"},
            {"name": "pomidorki koktajlowe", "quantity": 80, "unit": "g", "category": "warzywa"},
            {"name": "musztarda", "quantity": 1, "unit": "łyżeczka", "category": "inne"},
        ],
        "instructions": "1. Kurczaka piecz w air fryerze 200°C 12 min, pokrój w paski. "
                        "2. Wymieszaj z sałatą i pomidorkami, dopraw musztardą.",
    },
    {
        "id": 49, "name": "Zupa jarzynowa z Lidlomixa", "method": "lidlomix", "meal_type": "kolacja",
        "servings": 1, "calories": 210, "protein_g": 8, "fat_g": 5, "carbs_g": 32,
        "allergens": ["seler"],
        "ingredients": [
            {"name": "marchew", "quantity": 80, "unit": "g", "category": "warzywa"},
            {"name": "ziemniaki", "quantity": 100, "unit": "g", "category": "warzywa"},
            {"name": "pietruszka", "quantity": 40, "unit": "g", "category": "warzywa"},
            {"name": "seler korzeniowy", "quantity": 30, "unit": "g", "category": "warzywa"},
        ],
        "instructions": "1. Warzywa posiekaj programem (5 sek/pr.5). 2. Gotuj programem zupa 100°C 25 min.",
    },
    {
        "id": 50, "name": "Pieczone warzywa z serem feta z air fryera", "method": "air_fryer", "meal_type": "kolacja",
        "servings": 1, "calories": 310, "protein_g": 11, "fat_g": 20, "carbs_g": 22,
        "allergens": ["laktoza"],
        "ingredients": [
            {"name": "cukinia", "quantity": 100, "unit": "g", "category": "warzywa"},
            {"name": "papryka", "quantity": 100, "unit": "g", "category": "warzywa"},
            {"name": "bakłażan", "quantity": 100, "unit": "g", "category": "warzywa"},
            {"name": "ser feta", "quantity": 50, "unit": "g", "category": "nabial"},
        ],
        "instructions": "1. Warzywa pokrój w kostkę, skrop oliwą. 2. Piecz w air fryerze 190°C 12 min. "
                        "3. Posyp pokruszoną fetą.",
    },

    # ---------------------------------------------------------------- PRZEKASKI
    {
        "id": 60, "name": "Jabłko z masłem orzechowym", "method": "tradycyjne", "meal_type": "przekaska",
        "servings": 1, "calories": 180, "protein_g": 5, "fat_g": 10, "carbs_g": 20,
        "allergens": ["orzeszki_ziemne"],
        "ingredients": [
            {"name": "jabłko", "quantity": 1, "unit": "szt", "category": "owoce"},
            {"name": "masło orzechowe", "quantity": 15, "unit": "g", "category": "inne"},
        ],
        "instructions": "1. Jabłko pokrój w plastry. 2. Podawaj z masłem orzechowym do maczania.",
    },
    {
        "id": 61, "name": "Chipsy z jarmużu z air fryera", "method": "air_fryer", "meal_type": "przekaska",
        "servings": 1, "calories": 90, "protein_g": 3, "fat_g": 5, "carbs_g": 8,
        "allergens": [],
        "ingredients": [
            {"name": "jarmuż", "quantity": 60, "unit": "g", "category": "warzywa"},
            {"name": "oliwa z oliwek", "quantity": 5, "unit": "ml", "category": "inne"},
        ],
        "instructions": "1. Jarmuż wymieszaj z oliwą i solą. 2. Piecz w air fryerze 150°C 6-8 min.",
    },
    {
        "id": 62, "name": "Koktajl proteinowy", "method": "tradycyjne", "meal_type": "przekaska",
        "servings": 1, "calories": 200, "protein_g": 24, "fat_g": 4, "carbs_g": 18,
        "allergens": ["laktoza"],
        "ingredients": [
            {"name": "odzywka bialkowa", "quantity": 30, "unit": "g", "category": "inne"},
            {"name": "mleko", "quantity": 250, "unit": "ml", "category": "nabial"},
        ],
        "instructions": "1. Zmiksuj odżywkę z mlekiem.",
    },
    {
        "id": 63, "name": "Serek wiejski z ananasem", "method": "tradycyjne", "meal_type": "przekaska",
        "servings": 1, "calories": 170, "protein_g": 14, "fat_g": 4, "carbs_g": 20,
        "allergens": ["laktoza"],
        "ingredients": [
            {"name": "serek wiejski", "quantity": 150, "unit": "g", "category": "nabial"},
            {"name": "ananas", "quantity": 60, "unit": "g", "category": "owoce"},
        ],
        "instructions": "1. Wymieszaj serek wiejski z pokrojonym ananasem.",
    },
    {
        "id": 64, "name": "Orzechy i suszone owoce", "method": "tradycyjne", "meal_type": "przekaska",
        "servings": 1, "calories": 220, "protein_g": 6, "fat_g": 15, "carbs_g": 16,
        "allergens": ["orzechy"],
        "ingredients": [
            {"name": "migdały", "quantity": 20, "unit": "g", "category": "bakalie"},
            {"name": "morele suszone", "quantity": 20, "unit": "g", "category": "bakalie"},
        ],
        "instructions": "1. Wymieszaj migdały z suszonymi morelami.",
    },
    {
        "id": 65, "name": "Pieczone słupki marchewki z air fryera", "method": "air_fryer", "meal_type": "przekaska",
        "servings": 1, "calories": 120, "protein_g": 2, "fat_g": 5, "carbs_g": 16,
        "allergens": [],
        "ingredients": [
            {"name": "marchew", "quantity": 200, "unit": "g", "category": "warzywa"},
            {"name": "oliwa z oliwek", "quantity": 5, "unit": "ml", "category": "inne"},
        ],
        "instructions": "1. Marchew pokrój w słupki, skrop oliwą. 2. Piecz w air fryerze 180°C 10 min.",
    },
    {
        "id": 66, "name": "Hummus z chrupkim pieczywem", "method": "lidlomix", "meal_type": "przekaska",
        "servings": 1, "calories": 210, "protein_g": 8, "fat_g": 10, "carbs_g": 22,
        "allergens": ["sezam", "gluten"],
        "ingredients": [
            {"name": "ciecierzyca", "quantity": 100, "unit": "g", "category": "warzywa"},
            {"name": "tahini", "quantity": 10, "unit": "g", "category": "inne"},
            {"name": "pieczywo chrupkie", "quantity": 20, "unit": "g", "category": "pieczywo"},
        ],
        "instructions": "1. Zmiksuj ciecierzycę z tahini (30 sek/pr.8). 2. Podawaj z pieczywem chrupkim.",
    },
    {
        "id": 67, "name": "Jajko na twardo z solą i szczypiorkiem", "method": "tradycyjne", "meal_type": "przekaska",
        "servings": 1, "calories": 90, "protein_g": 7, "fat_g": 6, "carbs_g": 1,
        "allergens": ["jaja"],
        "ingredients": [
            {"name": "jajko", "quantity": 1, "unit": "szt", "category": "nabial"},
            {"name": "szczypiorek", "quantity": 1, "unit": "łyżeczka", "category": "warzywa"},
        ],
        "instructions": "1. Ugotuj jajko na twardo (8 min). 2. Posyp szczypiorkiem i solą.",
    },

    # ---------------------------------------------------------------- SNIADANIA (dodatkowe)
    {
        "id": 100, "name": "Tosty z serem i szynką", "method": "tradycyjne", "meal_type": "sniadanie",
        "servings": 1, "calories": 380, "protein_g": 20, "fat_g": 18, "carbs_g": 34,
        "allergens": ["gluten", "laktoza"],
        "ingredients": [
            {"name": "chleb tostowy", "quantity": 60, "unit": "g", "category": "pieczywo"},
            {"name": "szynka", "quantity": 40, "unit": "g", "category": "mięso"},
            {"name": "ser żółty", "quantity": 30, "unit": "g", "category": "nabial"},
            {"name": "masło", "quantity": 10, "unit": "g", "category": "nabial"},
        ],
        "instructions": "1. Posmaruj kromki masłem. 2. Ułóż szynkę i ser. 3. Opiecz na patelni lub w tosterze do rozpuszczenia sera.",
    },
    {
        "id": 101, "name": "Naleśniki z twarogiem", "method": "tradycyjne", "meal_type": "sniadanie",
        "servings": 1, "calories": 420, "protein_g": 20, "fat_g": 12, "carbs_g": 58,
        "allergens": ["gluten", "jaja", "laktoza"],
        "ingredients": [
            {"name": "mąka pszenna", "quantity": 60, "unit": "g", "category": "produkty sypkie"},
            {"name": "jajko", "quantity": 1, "unit": "szt", "category": "nabial"},
            {"name": "mleko", "quantity": 100, "unit": "ml", "category": "nabial"},
            {"name": "twarog polttusty", "quantity": 100, "unit": "g", "category": "nabial"},
            {"name": "cukier", "quantity": 1, "unit": "łyżeczka", "category": "inne"},
        ],
        "instructions": "1. Zmiksuj mąkę, jajko i mleko na ciasto. 2. Usmaż cienkie naleśniki. "
                        "3. Nadziewaj słodkim twarogiem i zwiń.",
    },
    {
        "id": 102, "name": "Owsianka na wodzie z jabłkiem i cynamonem", "method": "tradycyjne", "meal_type": "sniadanie",
        "servings": 1, "calories": 280, "protein_g": 8, "fat_g": 4, "carbs_g": 56,
        "allergens": ["gluten"],
        "ingredients": [
            {"name": "płatki owsiane", "quantity": 50, "unit": "g", "category": "produkty sypkie"},
            {"name": "jabłko", "quantity": 1, "unit": "szt", "category": "owoce"},
            {"name": "cynamon", "quantity": 1, "unit": "szczypta", "category": "przyprawy"},
            {"name": "miod", "quantity": 1, "unit": "łyżeczka", "category": "inne"},
        ],
        "instructions": "1. Ugotuj płatki owsiane na wodzie. 2. Dodaj starte jabłko i cynamon. 3. Polej miodem.",
    },
    {
        "id": 103, "name": "Frittata z warzywami z air fryera", "method": "air_fryer", "meal_type": "sniadanie",
        "servings": 1, "calories": 300, "protein_g": 21, "fat_g": 20, "carbs_g": 8,
        "allergens": ["jaja", "laktoza"],
        "ingredients": [
            {"name": "jajka", "quantity": 3, "unit": "szt", "category": "nabial"},
            {"name": "cukinia", "quantity": 80, "unit": "g", "category": "warzywa"},
            {"name": "papryka", "quantity": 50, "unit": "g", "category": "warzywa"},
            {"name": "ser żółty", "quantity": 20, "unit": "g", "category": "nabial"},
        ],
        "instructions": "1. Roztrzep jajka z pokrojonymi warzywami i serem. 2. Przelej do naczynia do air fryera. "
                        "3. Piecz 170°C ok. 12 min.",
    },
    {
        "id": 104, "name": "Kanapka z pastą z tuńczyka", "method": "tradycyjne", "meal_type": "sniadanie",
        "servings": 1, "calories": 320, "protein_g": 24, "fat_g": 8, "carbs_g": 36,
        "allergens": ["gluten", "ryby", "laktoza"],
        "ingredients": [
            {"name": "chleb razowy", "quantity": 60, "unit": "g", "category": "pieczywo"},
            {"name": "tuńczyk w sosie własnym", "quantity": 80, "unit": "g", "category": "ryby"},
            {"name": "jogurt naturalny", "quantity": 30, "unit": "g", "category": "nabial"},
            {"name": "papryka", "quantity": 30, "unit": "g", "category": "warzywa"},
        ],
        "instructions": "1. Wymieszaj tuńczyka z jogurtem i posiekaną papryką. 2. Nałóż na kromki chleba.",
    },
    {
        "id": 105, "name": "Musli z jogurtem i owocami", "method": "tradycyjne", "meal_type": "sniadanie",
        "servings": 1, "calories": 380, "protein_g": 14, "fat_g": 11, "carbs_g": 58,
        "allergens": ["gluten", "orzechy", "laktoza"],
        "ingredients": [
            {"name": "musli", "quantity": 50, "unit": "g", "category": "produkty sypkie"},
            {"name": "jogurt naturalny", "quantity": 200, "unit": "g", "category": "nabial"},
            {"name": "truskawki", "quantity": 80, "unit": "g", "category": "owoce"},
        ],
        "instructions": "1. Wymieszaj musli z jogurtem. 2. Dodaj pokrojone truskawki.",
    },
    {
        "id": 106, "name": "Jajka sadzone z awokado i pomidorem", "method": "tradycyjne", "meal_type": "sniadanie",
        "servings": 1, "calories": 340, "protein_g": 15, "fat_g": 26, "carbs_g": 10,
        "allergens": ["jaja", "laktoza"],
        "ingredients": [
            {"name": "jajka", "quantity": 2, "unit": "szt", "category": "nabial"},
            {"name": "awokado", "quantity": 0.5, "unit": "szt", "category": "warzywa"},
            {"name": "pomidor", "quantity": 1, "unit": "szt", "category": "warzywa"},
            {"name": "masło", "quantity": 5, "unit": "g", "category": "nabial"},
        ],
        "instructions": "1. Usmaż jajka sadzone na maśle. 2. Podawaj z plastrami awokado i pomidora.",
    },
    {
        "id": 107, "name": "Placki ziemniaczane z jogurtem", "method": "air_fryer", "meal_type": "sniadanie",
        "servings": 1, "calories": 350, "protein_g": 12, "fat_g": 8, "carbs_g": 58,
        "allergens": ["jaja", "gluten", "laktoza"],
        "ingredients": [
            {"name": "ziemniaki", "quantity": 250, "unit": "g", "category": "warzywa"},
            {"name": "jajko", "quantity": 1, "unit": "szt", "category": "nabial"},
            {"name": "mąka pszenna", "quantity": 20, "unit": "g", "category": "produkty sypkie"},
            {"name": "jogurt naturalny", "quantity": 50, "unit": "g", "category": "nabial"},
        ],
        "instructions": "1. Zetrzyj ziemniaki, wymieszaj z jajkiem i mąką. 2. Formuj placki i piecz w air fryerze 200°C 15 min, "
                        "przewracając w połowie. 3. Podawaj z jogurtem.",
    },
    {
        "id": 108, "name": "Owsianka na mleku owsianym z borówkami", "method": "tradycyjne", "meal_type": "sniadanie",
        "servings": 1, "calories": 300, "protein_g": 8, "fat_g": 6, "carbs_g": 54,
        "allergens": ["gluten"],
        "ingredients": [
            {"name": "płatki owsiane", "quantity": 50, "unit": "g", "category": "produkty sypkie"},
            {"name": "mleko owsiane", "quantity": 200, "unit": "ml", "category": "inne"},
            {"name": "borowki", "quantity": 80, "unit": "g", "category": "owoce"},
        ],
        "instructions": "1. Zagotuj mleko owsiane, wsyp płatki i gotuj 3-4 min. 2. Podawaj z borówkami.",
    },
    {
        "id": 109, "name": "Kanapka wegetariańska z hummusem", "method": "tradycyjne", "meal_type": "sniadanie",
        "servings": 1, "calories": 310, "protein_g": 10, "fat_g": 12, "carbs_g": 40,
        "allergens": ["gluten", "sezam"],
        "ingredients": [
            {"name": "chleb razowy", "quantity": 60, "unit": "g", "category": "pieczywo"},
            {"name": "hummus", "quantity": 60, "unit": "g", "category": "inne"},
            {"name": "papryka", "quantity": 50, "unit": "g", "category": "warzywa"},
        ],
        "instructions": "1. Posmaruj chleb hummusem. 2. Ułóż plastry papryki.",
    },
    {
        "id": 110, "name": "Szakszuka", "method": "tradycyjne", "meal_type": "sniadanie",
        "servings": 1, "calories": 280, "protein_g": 16, "fat_g": 16, "carbs_g": 16,
        "allergens": ["jaja"],
        "ingredients": [
            {"name": "jajka", "quantity": 2, "unit": "szt", "category": "nabial"},
            {"name": "pomidory", "quantity": 200, "unit": "g", "category": "warzywa"},
            {"name": "papryka", "quantity": 80, "unit": "g", "category": "warzywa"},
            {"name": "cebula", "quantity": 40, "unit": "g", "category": "warzywa"},
        ],
        "instructions": "1. Podduś cebulę i paprykę, dodaj pomidory i duś 10 min. 2. Zrób wgłębienia i wbij jajka. "
                        "3. Przykryj i gotuj do ścięcia białek.",
    },
    {
        "id": 111, "name": "Gofry proteinowe z air fryera", "method": "air_fryer", "meal_type": "sniadanie",
        "servings": 1, "calories": 340, "protein_g": 26, "fat_g": 8, "carbs_g": 38,
        "allergens": ["gluten", "jaja", "laktoza"],
        "ingredients": [
            {"name": "mąka pszenna", "quantity": 40, "unit": "g", "category": "produkty sypkie"},
            {"name": "jajko", "quantity": 1, "unit": "szt", "category": "nabial"},
            {"name": "odzywka bialkowa", "quantity": 20, "unit": "g", "category": "inne"},
            {"name": "mleko", "quantity": 100, "unit": "ml", "category": "nabial"},
        ],
        "instructions": "1. Zmiksuj składniki na ciasto. 2. Piecz w gofrownicy lub formie do air fryera 180°C ok. 8 min.",
    },
    {
        "id": 112, "name": "Twarożek z miodem i orzechami", "method": "tradycyjne", "meal_type": "sniadanie",
        "servings": 1, "calories": 300, "protein_g": 22, "fat_g": 14, "carbs_g": 20,
        "allergens": ["laktoza", "orzechy"],
        "ingredients": [
            {"name": "twarog polttusty", "quantity": 150, "unit": "g", "category": "nabial"},
            {"name": "miod", "quantity": 1, "unit": "łyżka", "category": "inne"},
            {"name": "orzechy wloskie", "quantity": 15, "unit": "g", "category": "bakalie"},
        ],
        "instructions": "1. Rozgnieć twaróg. 2. Polej miodem i posyp orzechami.",
    },
    {
        "id": 113, "name": "Kasza manna na mleku z owocami", "method": "tradycyjne", "meal_type": "sniadanie",
        "servings": 1, "calories": 340, "protein_g": 12, "fat_g": 7, "carbs_g": 58,
        "allergens": ["gluten", "laktoza"],
        "ingredients": [
            {"name": "kasza manna", "quantity": 50, "unit": "g", "category": "produkty sypkie"},
            {"name": "mleko", "quantity": 250, "unit": "ml", "category": "nabial"},
            {"name": "banan", "quantity": 1, "unit": "szt", "category": "owoce"},
        ],
        "instructions": "1. Zagotuj mleko, wsyp kaszę mannę cienkim strumieniem, mieszając. 2. Gotuj 3 min. "
                        "3. Podawaj z pokrojonym bananem.",
    },
    {
        "id": 114, "name": "Roladki z omletu z warzywami z Lidlomixa", "method": "lidlomix", "meal_type": "sniadanie",
        "servings": 1, "calories": 260, "protein_g": 19, "fat_g": 17, "carbs_g": 8,
        "allergens": ["jaja"],
        "ingredients": [
            {"name": "jajka", "quantity": 3, "unit": "szt", "category": "nabial"},
            {"name": "marchew", "quantity": 50, "unit": "g", "category": "warzywa"},
            {"name": "papryka", "quantity": 50, "unit": "g", "category": "warzywa"},
        ],
        "instructions": "1. Zetrzyj marchew, posiekaj paprykę programem (5 sek/pr.5). 2. Wymieszaj z jajkami, usmaż cienki omlet. "
                        "3. Nałóż warzywa i zwiń w roladkę.",
    },

    # ---------------------------------------------------------------- OBIADY (dodatkowe)
    {
        "id": 120, "name": "Pierogi ruskie gotowane", "method": "tradycyjne", "meal_type": "obiad",
        "servings": 1, "calories": 480, "protein_g": 16, "fat_g": 10, "carbs_g": 82,
        "allergens": ["gluten", "laktoza"],
        "ingredients": [
            {"name": "mąka pszenna", "quantity": 100, "unit": "g", "category": "produkty sypkie"},
            {"name": "ziemniaki", "quantity": 150, "unit": "g", "category": "warzywa"},
            {"name": "twarog polttusty", "quantity": 80, "unit": "g", "category": "nabial"},
            {"name": "cebula", "quantity": 40, "unit": "g", "category": "warzywa"},
        ],
        "instructions": "1. Zagnieć ciasto z mąki i wody. 2. Nadziewaj purée ziemniaczanym z twarogiem i cebulką. "
                        "3. Gotuj w osolonej wodzie do wypłynięcia.",
    },
    {
        "id": 121, "name": "Risotto z kurczakiem z Lidlomixa", "method": "lidlomix", "meal_type": "obiad",
        "servings": 1, "calories": 460, "protein_g": 32, "fat_g": 12, "carbs_g": 56,
        "allergens": ["laktoza"],
        "ingredients": [
            {"name": "ryż arborio", "quantity": 80, "unit": "g", "category": "produkty sypkie"},
            {"name": "pierś z kurczaka", "quantity": 120, "unit": "g", "category": "mięso"},
            {"name": "bulion warzywny", "quantity": 200, "unit": "ml", "category": "inne"},
            {"name": "parmezan", "quantity": 20, "unit": "g", "category": "nabial"},
        ],
        "instructions": "1. Podsmaż kurczaka programem 120°C 8 min. 2. Dodaj ryż i bulion, gotuj programem risotto 18 min. "
                        "3. Wymieszaj z parmezanem.",
    },
    {
        "id": 122, "name": "Kurczak w curry z ryżem", "method": "tradycyjne", "meal_type": "obiad",
        "servings": 1, "calories": 480, "protein_g": 34, "fat_g": 16, "carbs_g": 50,
        "allergens": [],
        "ingredients": [
            {"name": "pierś z kurczaka", "quantity": 150, "unit": "g", "category": "mięso"},
            {"name": "mleko kokosowe", "quantity": 100, "unit": "ml", "category": "inne"},
            {"name": "curry przyprawa", "quantity": 1, "unit": "łyżeczka", "category": "przyprawy"},
            {"name": "ryż", "quantity": 70, "unit": "g", "category": "produkty sypkie"},
        ],
        "instructions": "1. Podsmaż kurczaka pokrojonego w kostkę. 2. Dodaj mleko kokosowe i curry, duś 15 min. "
                        "3. Podawaj z ryżem.",
    },
    {
        "id": 123, "name": "Pieczony łosoś z kaszą gryczaną z air fryera", "method": "air_fryer", "meal_type": "obiad",
        "servings": 1, "calories": 460, "protein_g": 34, "fat_g": 20, "carbs_g": 34,
        "allergens": ["ryby"],
        "ingredients": [
            {"name": "filet z łososia", "quantity": 150, "unit": "g", "category": "ryby"},
            {"name": "kasza gryczana", "quantity": 70, "unit": "g", "category": "produkty sypkie"},
            {"name": "cytryna", "quantity": 0.5, "unit": "szt", "category": "owoce"},
        ],
        "instructions": "1. Łososia skrop cytryną, przypraw. 2. Piecz w air fryerze 200°C 10 min. "
                        "3. Podawaj z ugotowaną kaszą gryczaną.",
    },
    {
        "id": 124, "name": "Gołąbki z ryżem i mięsem", "method": "tradycyjne", "meal_type": "obiad",
        "servings": 1, "calories": 440, "protein_g": 26, "fat_g": 18, "carbs_g": 42,
        "allergens": [],
        "ingredients": [
            {"name": "kapusta biała", "quantity": 200, "unit": "g", "category": "warzywa"},
            {"name": "ryż", "quantity": 50, "unit": "g", "category": "produkty sypkie"},
            {"name": "mięso mielone wieprzowo-wołowe", "quantity": 120, "unit": "g", "category": "mięso"},
            {"name": "cebula", "quantity": 30, "unit": "g", "category": "warzywa"},
        ],
        "instructions": "1. Sparz liście kapusty. 2. Wymieszaj ryż, mięso i cebulę, zawiń w liście. "
                        "3. Duś w sosie pomidorowym ok. 40 min.",
    },
    {
        "id": 125, "name": "Makaron z pesto i kurczakiem", "method": "tradycyjne", "meal_type": "obiad",
        "servings": 1, "calories": 540, "protein_g": 36, "fat_g": 20, "carbs_g": 54,
        "allergens": ["gluten", "orzechy", "laktoza"],
        "ingredients": [
            {"name": "makaron", "quantity": 80, "unit": "g", "category": "produkty sypkie"},
            {"name": "pierś z kurczaka", "quantity": 120, "unit": "g", "category": "mięso"},
            {"name": "pesto", "quantity": 30, "unit": "g", "category": "inne"},
            {"name": "parmezan", "quantity": 15, "unit": "g", "category": "nabial"},
        ],
        "instructions": "1. Ugotuj makaron. 2. Podsmaż kurczaka pokrojonego w paski. "
                        "3. Wymieszaj makaron, kurczaka i pesto, posyp parmezanem.",
    },
    {
        "id": 126, "name": "Zapiekanka warzywna z serem z air fryera", "method": "air_fryer", "meal_type": "obiad",
        "servings": 1, "calories": 340, "protein_g": 18, "fat_g": 20, "carbs_g": 20,
        "allergens": ["laktoza"],
        "ingredients": [
            {"name": "cukinia", "quantity": 100, "unit": "g", "category": "warzywa"},
            {"name": "papryka", "quantity": 100, "unit": "g", "category": "warzywa"},
            {"name": "pomidor", "quantity": 100, "unit": "g", "category": "warzywa"},
            {"name": "ser żółty", "quantity": 60, "unit": "g", "category": "nabial"},
        ],
        "instructions": "1. Ułóż pokrojone warzywa w naczyniu, posyp serem. 2. Piecz w air fryerze 180°C 15 min.",
    },
    {
        "id": 127, "name": "Kotlet schabowy pieczony z ziemniakami z air fryera", "method": "air_fryer", "meal_type": "obiad",
        "servings": 1, "calories": 520, "protein_g": 40, "fat_g": 20, "carbs_g": 44,
        "allergens": ["jaja", "gluten"],
        "ingredients": [
            {"name": "schab", "quantity": 150, "unit": "g", "category": "mięso"},
            {"name": "jajko", "quantity": 1, "unit": "szt", "category": "nabial"},
            {"name": "bułka tarta", "quantity": 25, "unit": "g", "category": "produkty sypkie"},
            {"name": "ziemniaki", "quantity": 200, "unit": "g", "category": "warzywa"},
        ],
        "instructions": "1. Rozbij schab, panieruj w jajku i bułce tartej. 2. Piecz w air fryerze 190°C 14 min. "
                        "3. Ziemniaki piecz osobno 180°C 15 min.",
    },
    {
        "id": 128, "name": "Pad thai z kurczakiem", "method": "tradycyjne", "meal_type": "obiad",
        "servings": 1, "calories": 520, "protein_g": 34, "fat_g": 16, "carbs_g": 58,
        "allergens": ["jaja", "orzeszki_ziemne", "soja", "gluten"],
        "ingredients": [
            {"name": "makaron ryżowy", "quantity": 80, "unit": "g", "category": "produkty sypkie"},
            {"name": "pierś z kurczaka", "quantity": 120, "unit": "g", "category": "mięso"},
            {"name": "orzeszki ziemne", "quantity": 20, "unit": "g", "category": "bakalie"},
            {"name": "jajko", "quantity": 1, "unit": "szt", "category": "nabial"},
            {"name": "sos sojowy", "quantity": 15, "unit": "ml", "category": "inne"},
        ],
        "instructions": "1. Namocz makaron ryżowy. 2. Podsmaż kurczaka i jajko, dodaj makaron i sos sojowy. "
                        "3. Posyp zmielonymi orzeszkami.",
    },
    {
        "id": 129, "name": "Gulasz węgierski z Lidlomixa", "method": "lidlomix", "meal_type": "obiad",
        "servings": 1, "calories": 460, "protein_g": 32, "fat_g": 18, "carbs_g": 38,
        "allergens": [],
        "ingredients": [
            {"name": "wołowina gulaszowa", "quantity": 150, "unit": "g", "category": "mięso"},
            {"name": "papryka", "quantity": 100, "unit": "g", "category": "warzywa"},
            {"name": "cebula", "quantity": 50, "unit": "g", "category": "warzywa"},
            {"name": "ziemniaki", "quantity": 100, "unit": "g", "category": "warzywa"},
        ],
        "instructions": "1. Podsmaż mięso i cebulę programem 120°C 10 min. 2. Dodaj paprykę i ziemniaki, "
                        "duś programem 90°C 40 min.",
    },
    {
        "id": 130, "name": "Kasza gryczana z pieczarkami i cebulą", "method": "tradycyjne", "meal_type": "obiad",
        "servings": 1, "calories": 380, "protein_g": 12, "fat_g": 12, "carbs_g": 54,
        "allergens": ["laktoza"],
        "ingredients": [
            {"name": "kasza gryczana", "quantity": 80, "unit": "g", "category": "produkty sypkie"},
            {"name": "pieczarki", "quantity": 150, "unit": "g", "category": "warzywa"},
            {"name": "cebula", "quantity": 50, "unit": "g", "category": "warzywa"},
            {"name": "masło", "quantity": 15, "unit": "g", "category": "nabial"},
        ],
        "instructions": "1. Ugotuj kaszę gryczaną. 2. Podsmaż pieczarki z cebulą na maśle. 3. Wymieszaj z kaszą.",
    },
    {
        "id": 131, "name": "Pieczone udka z kaczki z jabłkiem z air fryera", "method": "air_fryer", "meal_type": "obiad",
        "servings": 1, "calories": 480, "protein_g": 34, "fat_g": 30, "carbs_g": 18,
        "allergens": [],
        "ingredients": [
            {"name": "udka z kaczki", "quantity": 200, "unit": "g", "category": "mięso"},
            {"name": "jabłko", "quantity": 1, "unit": "szt", "category": "owoce"},
        ],
        "instructions": "1. Udka natnij ze skóry, przypraw. 2. Piecz w air fryerze 180°C 20 min. "
                        "3. Jabłko piecz obok ostatnie 10 min.",
    },
    {
        "id": 132, "name": "Makaron carbonara", "method": "tradycyjne", "meal_type": "obiad",
        "servings": 1, "calories": 560, "protein_g": 26, "fat_g": 26, "carbs_g": 54,
        "allergens": ["gluten", "jaja", "laktoza"],
        "ingredients": [
            {"name": "makaron spaghetti", "quantity": 80, "unit": "g", "category": "produkty sypkie"},
            {"name": "boczek", "quantity": 60, "unit": "g", "category": "mięso"},
            {"name": "jajka", "quantity": 2, "unit": "szt", "category": "nabial"},
            {"name": "parmezan", "quantity": 20, "unit": "g", "category": "nabial"},
        ],
        "instructions": "1. Ugotuj makaron. 2. Podsmaż boczek. 3. Wymieszaj gorący makaron z boczkiem, jajkami i parmezanem poza ogniem.",
    },
    {
        "id": 133, "name": "Kurczak teriyaki z ryżem z Lidlomixa", "method": "lidlomix", "meal_type": "obiad",
        "servings": 1, "calories": 460, "protein_g": 36, "fat_g": 10, "carbs_g": 54,
        "allergens": ["soja", "sezam", "gluten"],
        "ingredients": [
            {"name": "pierś z kurczaka", "quantity": 150, "unit": "g", "category": "mięso"},
            {"name": "sos sojowy", "quantity": 20, "unit": "ml", "category": "inne"},
            {"name": "ryż", "quantity": 70, "unit": "g", "category": "produkty sypkie"},
            {"name": "sezam", "quantity": 5, "unit": "g", "category": "przyprawy"},
        ],
        "instructions": "1. Podsmaż kurczaka programem 120°C 10 min. 2. Dodaj sos sojowy, duś 5 min. "
                        "3. Podawaj z ryżem, posyp sezamem.",
    },
    {
        "id": 134, "name": "Zupa krem z soczewicy z Lidlomixa", "method": "lidlomix", "meal_type": "obiad",
        "servings": 1, "calories": 320, "protein_g": 18, "fat_g": 4, "carbs_g": 52,
        "allergens": [],
        "ingredients": [
            {"name": "soczewica czerwona", "quantity": 100, "unit": "g", "category": "warzywa"},
            {"name": "marchew", "quantity": 60, "unit": "g", "category": "warzywa"},
            {"name": "cebula", "quantity": 40, "unit": "g", "category": "warzywa"},
            {"name": "bulion warzywny", "quantity": 200, "unit": "ml", "category": "inne"},
        ],
        "instructions": "1. Warzywa i soczewicę gotuj z bulionem programem zupa 100°C 20 min. 2. Zmiksuj programem 30 sek/pr.8.",
    },
    {
        "id": 135, "name": "Pieczony bakłażan faszerowany z air fryera", "method": "air_fryer", "meal_type": "obiad",
        "servings": 1, "calories": 400, "protein_g": 24, "fat_g": 22, "carbs_g": 20,
        "allergens": ["laktoza"],
        "ingredients": [
            {"name": "bakłażan", "quantity": 200, "unit": "g", "category": "warzywa"},
            {"name": "mięso mielone wołowe", "quantity": 100, "unit": "g", "category": "mięso"},
            {"name": "pomidor", "quantity": 80, "unit": "g", "category": "warzywa"},
            {"name": "ser żółty", "quantity": 30, "unit": "g", "category": "nabial"},
        ],
        "instructions": "1. Przekrój bakłażana, wydrąż środek. 2. Nadziej podsmażonym mięsem z pomidorem, posyp serem. "
                        "3. Piecz w air fryerze 190°C 15 min.",
    },
    {
        "id": 136, "name": "Ryba po grecku", "method": "tradycyjne", "meal_type": "obiad",
        "servings": 1, "calories": 340, "protein_g": 32, "fat_g": 10, "carbs_g": 26,
        "allergens": ["ryby"],
        "ingredients": [
            {"name": "filet z dorsza", "quantity": 180, "unit": "g", "category": "ryby"},
            {"name": "marchew", "quantity": 100, "unit": "g", "category": "warzywa"},
            {"name": "cebula", "quantity": 50, "unit": "g", "category": "warzywa"},
            {"name": "koncentrat pomidorowy", "quantity": 30, "unit": "g", "category": "inne"},
        ],
        "instructions": "1. Obsmaż rybę. 2. Warzywa poduś z koncentratem pomidorowym. 3. Polej rybę sosem warzywnym.",
    },
    {
        "id": 137, "name": "Kotlet mielony z indyka z kaszą jaglaną z air fryera", "method": "air_fryer", "meal_type": "obiad",
        "servings": 1, "calories": 420, "protein_g": 36, "fat_g": 12, "carbs_g": 42,
        "allergens": ["jaja"],
        "ingredients": [
            {"name": "mięso mielone z indyka", "quantity": 150, "unit": "g", "category": "mięso"},
            {"name": "jajko", "quantity": 1, "unit": "szt", "category": "nabial"},
            {"name": "kasza jaglana", "quantity": 70, "unit": "g", "category": "produkty sypkie"},
        ],
        "instructions": "1. Wymieszaj mięso z jajkiem, uformuj kotlety. 2. Piecz w air fryerze 190°C 12 min. "
                        "3. Podawaj z ugotowaną kaszą jaglaną.",
    },
    {
        "id": 138, "name": "Placki z cukinii z jogurtowym sosem", "method": "air_fryer", "meal_type": "obiad",
        "servings": 1, "calories": 300, "protein_g": 14, "fat_g": 10, "carbs_g": 36,
        "allergens": ["jaja", "gluten", "laktoza"],
        "ingredients": [
            {"name": "cukinia", "quantity": 200, "unit": "g", "category": "warzywa"},
            {"name": "jajko", "quantity": 1, "unit": "szt", "category": "nabial"},
            {"name": "mąka pszenna", "quantity": 30, "unit": "g", "category": "produkty sypkie"},
            {"name": "jogurt naturalny", "quantity": 50, "unit": "g", "category": "nabial"},
        ],
        "instructions": "1. Zetrzyj cukinię, odciśnij nadmiar wody. 2. Wymieszaj z jajkiem i mąką, formuj placki. "
                        "3. Piecz w air fryerze 190°C 12 min. 4. Podawaj z jogurtem.",
    },
    {
        "id": 139, "name": "Vege burger z ciecierzycy z air fryera", "method": "air_fryer", "meal_type": "obiad",
        "servings": 1, "calories": 420, "protein_g": 16, "fat_g": 10, "carbs_g": 62,
        "allergens": ["gluten"],
        "ingredients": [
            {"name": "ciecierzyca", "quantity": 150, "unit": "g", "category": "warzywa"},
            {"name": "bułka pszenna", "quantity": 60, "unit": "g", "category": "pieczywo"},
            {"name": "sałata", "quantity": 20, "unit": "g", "category": "warzywa"},
            {"name": "pomidor", "quantity": 50, "unit": "g", "category": "warzywa"},
        ],
        "instructions": "1. Zmiksuj ciecierzycę z przyprawami, uformuj kotlet. 2. Piecz w air fryerze 190°C 12 min. "
                        "3. Podawaj w bułce z sałatą i pomidorem.",
    },

    # ---------------------------------------------------------------- KOLACJE (dodatkowe)
    {
        "id": 140, "name": "Tortilla z kurczakiem i warzywami", "method": "tradycyjne", "meal_type": "kolacja",
        "servings": 1, "calories": 380, "protein_g": 28, "fat_g": 12, "carbs_g": 40,
        "allergens": ["gluten"],
        "ingredients": [
            {"name": "tortilla pszenna", "quantity": 60, "unit": "g", "category": "pieczywo"},
            {"name": "pierś z kurczaka", "quantity": 100, "unit": "g", "category": "mięso"},
            {"name": "papryka", "quantity": 60, "unit": "g", "category": "warzywa"},
            {"name": "sałata", "quantity": 30, "unit": "g", "category": "warzywa"},
        ],
        "instructions": "1. Podsmaż pokrojonego kurczaka z papryką. 2. Zawiń w tortillę z sałatą.",
    },
    {
        "id": 141, "name": "Zapiekane jajka w awokado z air fryera", "method": "air_fryer", "meal_type": "kolacja",
        "servings": 1, "calories": 360, "protein_g": 15, "fat_g": 30, "carbs_g": 8,
        "allergens": ["jaja"],
        "ingredients": [
            {"name": "jajka", "quantity": 2, "unit": "szt", "category": "nabial"},
            {"name": "awokado", "quantity": 1, "unit": "szt", "category": "warzywa"},
        ],
        "instructions": "1. Przekrój awokado, usuń trochę miąższu. 2. Wbij jajko w każdą połówkę. "
                        "3. Piecz w air fryerze 160°C 10-12 min.",
    },
    {
        "id": 142, "name": "Sałatka z komosy ryżowej i fetą", "method": "tradycyjne", "meal_type": "kolacja",
        "servings": 1, "calories": 380, "protein_g": 14, "fat_g": 20, "carbs_g": 36,
        "allergens": ["laktoza"],
        "ingredients": [
            {"name": "komosa ryżowa", "quantity": 60, "unit": "g", "category": "produkty sypkie"},
            {"name": "ser feta", "quantity": 60, "unit": "g", "category": "nabial"},
            {"name": "pomidorki koktajlowe", "quantity": 80, "unit": "g", "category": "warzywa"},
            {"name": "oliwki", "quantity": 20, "unit": "g", "category": "inne"},
        ],
        "instructions": "1. Ugotuj komosę ryżową. 2. Wymieszaj z pomidorkami, fetą i oliwkami.",
    },
    {
        "id": 143, "name": "Krewetki w sosie czosnkowo-cytrynowym z Lidlomixa", "method": "lidlomix", "meal_type": "kolacja",
        "servings": 1, "calories": 280, "protein_g": 28, "fat_g": 14, "carbs_g": 6,
        "allergens": ["skorupiaki", "laktoza"],
        "ingredients": [
            {"name": "krewetki", "quantity": 180, "unit": "g", "category": "ryby"},
            {"name": "czosnek", "quantity": 2, "unit": "ząbki", "category": "warzywa"},
            {"name": "cytryna", "quantity": 0.5, "unit": "szt", "category": "owoce"},
            {"name": "masło", "quantity": 10, "unit": "g", "category": "nabial"},
        ],
        "instructions": "1. Roztop masło z czosnkiem programem 100°C 3 min. 2. Dodaj krewetki, gotuj 5 min. "
                        "3. Skrop cytryną.",
    },
    {
        "id": 144, "name": "Kanapki z pastą z awokado i wędzonym łososiem", "method": "tradycyjne", "meal_type": "kolacja",
        "servings": 1, "calories": 360, "protein_g": 18, "fat_g": 20, "carbs_g": 28,
        "allergens": ["gluten", "ryby"],
        "ingredients": [
            {"name": "chleb razowy", "quantity": 50, "unit": "g", "category": "pieczywo"},
            {"name": "awokado", "quantity": 0.5, "unit": "szt", "category": "warzywa"},
            {"name": "łosoś wędzony", "quantity": 60, "unit": "g", "category": "ryby"},
        ],
        "instructions": "1. Rozgnieć awokado na chlebie. 2. Ułóż plastry wędzonego łososia.",
    },
    {
        "id": 145, "name": "Sałatka caprese", "method": "tradycyjne", "meal_type": "kolacja",
        "servings": 1, "calories": 320, "protein_g": 18, "fat_g": 24, "carbs_g": 8,
        "allergens": ["laktoza"],
        "ingredients": [
            {"name": "mozzarella", "quantity": 100, "unit": "g", "category": "nabial"},
            {"name": "pomidor", "quantity": 150, "unit": "g", "category": "warzywa"},
            {"name": "bazylia", "quantity": 1, "unit": "łyżka", "category": "przyprawy"},
            {"name": "oliwa z oliwek", "quantity": 10, "unit": "ml", "category": "inne"},
        ],
        "instructions": "1. Pokrój mozzarellę i pomidora w plastry, ułóż na przemian. 2. Posyp bazylią, skrop oliwą.",
    },
    {
        "id": 146, "name": "Zupa miso z tofu", "method": "lidlomix", "meal_type": "kolacja",
        "servings": 1, "calories": 200, "protein_g": 14, "fat_g": 9, "carbs_g": 14,
        "allergens": ["soja"],
        "ingredients": [
            {"name": "tofu", "quantity": 100, "unit": "g", "category": "warzywa"},
            {"name": "pasta miso", "quantity": 20, "unit": "g", "category": "inne"},
            {"name": "wodorosty nori", "quantity": 5, "unit": "g", "category": "inne"},
            {"name": "dymka", "quantity": 1, "unit": "łyżka", "category": "warzywa"},
        ],
        "instructions": "1. Zagotuj wodę, rozpuść pastę miso. 2. Dodaj kostki tofu i wodorosty, gotuj 3 min. "
                        "3. Posyp dymką.",
    },
    {
        "id": 147, "name": "Placki owsiane z serem i szynką z air fryera", "method": "air_fryer", "meal_type": "kolacja",
        "servings": 1, "calories": 380, "protein_g": 24, "fat_g": 18, "carbs_g": 30,
        "allergens": ["gluten", "jaja", "laktoza"],
        "ingredients": [
            {"name": "płatki owsiane", "quantity": 50, "unit": "g", "category": "produkty sypkie"},
            {"name": "jajko", "quantity": 1, "unit": "szt", "category": "nabial"},
            {"name": "ser żółty", "quantity": 30, "unit": "g", "category": "nabial"},
            {"name": "szynka", "quantity": 40, "unit": "g", "category": "mięso"},
        ],
        "instructions": "1. Zmiksuj płatki z jajkiem. 2. Wymieszaj z pokrojonym serem i szynką, uformuj placki. "
                        "3. Piecz w air fryerze 180°C 10 min.",
    },
    {
        "id": 148, "name": "Pieczony camembert w panierce z żurawiną z air fryera", "method": "air_fryer", "meal_type": "kolacja",
        "servings": 1, "calories": 420, "protein_g": 20, "fat_g": 28, "carbs_g": 22,
        "allergens": ["laktoza", "gluten", "jaja"],
        "ingredients": [
            {"name": "camembert", "quantity": 100, "unit": "g", "category": "nabial"},
            {"name": "bułka tarta", "quantity": 20, "unit": "g", "category": "produkty sypkie"},
            {"name": "jajko", "quantity": 1, "unit": "szt", "category": "nabial"},
            {"name": "żurawina suszona", "quantity": 20, "unit": "g", "category": "bakalie"},
        ],
        "instructions": "1. Camembert panieruj w jajku i bułce tartej. 2. Piecz w air fryerze 180°C 8 min. "
                        "3. Podawaj z żurawiną.",
    },
    {
        "id": 149, "name": "Sałatka z pieczonym burakiem i kozim serem", "method": "tradycyjne", "meal_type": "kolacja",
        "servings": 1, "calories": 320, "protein_g": 12, "fat_g": 22, "carbs_g": 18,
        "allergens": ["laktoza", "orzechy"],
        "ingredients": [
            {"name": "burak", "quantity": 150, "unit": "g", "category": "warzywa"},
            {"name": "ser kozi", "quantity": 50, "unit": "g", "category": "nabial"},
            {"name": "orzechy wloskie", "quantity": 15, "unit": "g", "category": "bakalie"},
            {"name": "rukola", "quantity": 30, "unit": "g", "category": "warzywa"},
        ],
        "instructions": "1. Upieczonego buraka pokrój w plastry. 2. Ułóż na rukoli z serem kozim i orzechami.",
    },
    {
        "id": 150, "name": "Roladki z szynki z serem i rzodkiewką", "method": "tradycyjne", "meal_type": "kolacja",
        "servings": 1, "calories": 260, "protein_g": 22, "fat_g": 16, "carbs_g": 6,
        "allergens": ["laktoza"],
        "ingredients": [
            {"name": "szynka", "quantity": 100, "unit": "g", "category": "mięso"},
            {"name": "serek topiony", "quantity": 40, "unit": "g", "category": "nabial"},
            {"name": "rzodkiewka", "quantity": 5, "unit": "szt", "category": "warzywa"},
        ],
        "instructions": "1. Posmaruj plastry szynki serkiem topionym. 2. Ułóż pokrojoną rzodkiewkę i zwiń w roladki.",
    },
    {
        "id": 151, "name": "Zupa krem z cukinii z Lidlomixa", "method": "lidlomix", "meal_type": "kolacja",
        "servings": 1, "calories": 220, "protein_g": 6, "fat_g": 12, "carbs_g": 20,
        "allergens": ["laktoza"],
        "ingredients": [
            {"name": "cukinia", "quantity": 250, "unit": "g", "category": "warzywa"},
            {"name": "cebula", "quantity": 40, "unit": "g", "category": "warzywa"},
            {"name": "śmietanka 12%", "quantity": 40, "unit": "ml", "category": "nabial"},
        ],
        "instructions": "1. Gotuj cukinię z cebulą programem zupa 100°C 20 min. 2. Zmiksuj z dodatkiem śmietanki.",
    },
    {
        "id": 152, "name": "Kanapka z pastą jajeczno-szczypiorkową na chlebie żytnim", "method": "tradycyjne", "meal_type": "kolacja",
        "servings": 1, "calories": 340, "protein_g": 16, "fat_g": 16, "carbs_g": 32,
        "allergens": ["gluten", "jaja", "gorczyca"],
        "ingredients": [
            {"name": "chleb żytni", "quantity": 50, "unit": "g", "category": "pieczywo"},
            {"name": "jajka", "quantity": 2, "unit": "szt", "category": "nabial"},
            {"name": "majonez", "quantity": 15, "unit": "g", "category": "inne"},
            {"name": "szczypiorek", "quantity": 1, "unit": "łyżka", "category": "warzywa"},
        ],
        "instructions": "1. Ugotuj jajka na twardo, zetrzyj. 2. Wymieszaj z majonezem i szczypiorkiem. "
                        "3. Nałóż na kromki chleba żytniego.",
    },
    {
        "id": 153, "name": "Sałatka z kurczakiem, awokado i kukurydzą", "method": "tradycyjne", "meal_type": "kolacja",
        "servings": 1, "calories": 380, "protein_g": 30, "fat_g": 20, "carbs_g": 22,
        "allergens": [],
        "ingredients": [
            {"name": "pierś z kurczaka", "quantity": 120, "unit": "g", "category": "mięso"},
            {"name": "awokado", "quantity": 0.5, "unit": "szt", "category": "warzywa"},
            {"name": "kukurydza", "quantity": 60, "unit": "g", "category": "warzywa"},
            {"name": "sałata", "quantity": 40, "unit": "g", "category": "warzywa"},
        ],
        "instructions": "1. Upiecz lub usmaż kurczaka, pokrój w paski. 2. Wymieszaj z sałatą, awokado i kukurydzą.",
    },
    {
        "id": 154, "name": "Pieczone warzywa korzeniowe z hummusem z air fryera", "method": "air_fryer", "meal_type": "kolacja",
        "servings": 1, "calories": 300, "protein_g": 9, "fat_g": 12, "carbs_g": 40,
        "allergens": ["sezam"],
        "ingredients": [
            {"name": "marchew", "quantity": 100, "unit": "g", "category": "warzywa"},
            {"name": "pietruszka", "quantity": 80, "unit": "g", "category": "warzywa"},
            {"name": "burak", "quantity": 80, "unit": "g", "category": "warzywa"},
            {"name": "hummus", "quantity": 60, "unit": "g", "category": "inne"},
        ],
        "instructions": "1. Pokrój warzywa korzeniowe w słupki, skrop oliwą. 2. Piecz w air fryerze 190°C 15 min. "
                        "3. Podawaj z hummusem.",
    },

    # ---------------------------------------------------------------- PRZEKASKI (dodatkowe)
    {
        "id": 160, "name": "Domowy batonik owocowo-orzechowy", "method": "tradycyjne", "meal_type": "przekaska",
        "servings": 1, "calories": 220, "protein_g": 5, "fat_g": 11, "carbs_g": 28,
        "allergens": ["orzechy", "gluten"],
        "ingredients": [
            {"name": "daktyle", "quantity": 40, "unit": "g", "category": "bakalie"},
            {"name": "orzechy wloskie", "quantity": 20, "unit": "g", "category": "bakalie"},
            {"name": "płatki owsiane", "quantity": 20, "unit": "g", "category": "produkty sypkie"},
        ],
        "instructions": "1. Zmiksuj daktyle z orzechami i płatkami. 2. Uformuj batonik i schłodź w lodówce.",
    },
    {
        "id": 161, "name": "Chipsy z buraka z air fryera", "method": "air_fryer", "meal_type": "przekaska",
        "servings": 1, "calories": 110, "protein_g": 2, "fat_g": 5, "carbs_g": 15,
        "allergens": [],
        "ingredients": [
            {"name": "burak", "quantity": 200, "unit": "g", "category": "warzywa"},
            {"name": "oliwa z oliwek", "quantity": 5, "unit": "ml", "category": "inne"},
        ],
        "instructions": "1. Pokrój buraka w cienkie plastry, skrop oliwą. 2. Piecz w air fryerze 160°C 12-15 min.",
    },
    {
        "id": 162, "name": "Jogurt grecki z miodem i orzechami", "method": "tradycyjne", "meal_type": "przekaska",
        "servings": 1, "calories": 210, "protein_g": 12, "fat_g": 12, "carbs_g": 16,
        "allergens": ["laktoza", "orzechy"],
        "ingredients": [
            {"name": "jogurt grecki", "quantity": 150, "unit": "g", "category": "nabial"},
            {"name": "miod", "quantity": 1, "unit": "łyżeczka", "category": "inne"},
            {"name": "orzechy wloskie", "quantity": 10, "unit": "g", "category": "bakalie"},
        ],
        "instructions": "1. Jogurt przelej do miski. 2. Polej miodem i posyp orzechami.",
    },
    {
        "id": 163, "name": "Serek wiejski z rzodkiewką i szczypiorkiem", "method": "tradycyjne", "meal_type": "przekaska",
        "servings": 1, "calories": 160, "protein_g": 15, "fat_g": 5, "carbs_g": 12,
        "allergens": ["laktoza"],
        "ingredients": [
            {"name": "serek wiejski", "quantity": 150, "unit": "g", "category": "nabial"},
            {"name": "rzodkiewka", "quantity": 4, "unit": "szt", "category": "warzywa"},
            {"name": "szczypiorek", "quantity": 1, "unit": "łyżka", "category": "warzywa"},
        ],
        "instructions": "1. Pokrój rzodkiewkę w plasterki. 2. Wymieszaj z serkiem wiejskim i szczypiorkiem.",
    },
    {
        "id": 164, "name": "Grissini z hummusem", "method": "tradycyjne", "meal_type": "przekaska",
        "servings": 1, "calories": 200, "protein_g": 7, "fat_g": 9, "carbs_g": 24,
        "allergens": ["gluten", "sezam"],
        "ingredients": [
            {"name": "grissini", "quantity": 30, "unit": "g", "category": "pieczywo"},
            {"name": "hummus", "quantity": 60, "unit": "g", "category": "inne"},
        ],
        "instructions": "1. Podawaj grissini z hummusem do maczania.",
    },
    {
        "id": 165, "name": "Smoothie bowl z owocami i granolą", "method": "tradycyjne", "meal_type": "przekaska",
        "servings": 1, "calories": 320, "protein_g": 12, "fat_g": 8, "carbs_g": 52,
        "allergens": ["laktoza", "gluten"],
        "ingredients": [
            {"name": "jogurt naturalny", "quantity": 150, "unit": "g", "category": "nabial"},
            {"name": "banan", "quantity": 1, "unit": "szt", "category": "owoce"},
            {"name": "granola", "quantity": 30, "unit": "g", "category": "produkty sypkie"},
            {"name": "maliny", "quantity": 50, "unit": "g", "category": "owoce"},
        ],
        "instructions": "1. Zmiksuj jogurt z połową banana. 2. Przelej do miski, udekoruj resztą banana, malinami i granolą.",
    },
    {
        "id": 166, "name": "Pieczone jabłko z cynamonem z air fryera", "method": "air_fryer", "meal_type": "przekaska",
        "servings": 1, "calories": 130, "protein_g": 1, "fat_g": 0, "carbs_g": 32,
        "allergens": [],
        "ingredients": [
            {"name": "jabłko", "quantity": 1, "unit": "szt", "category": "owoce"},
            {"name": "cynamon", "quantity": 1, "unit": "szczypta", "category": "przyprawy"},
            {"name": "miod", "quantity": 1, "unit": "łyżeczka", "category": "inne"},
        ],
        "instructions": "1. Wydrąż środek jabłka, posyp cynamonem i polej miodem. 2. Piecz w air fryerze 180°C 12 min.",
    },
    {
        "id": 167, "name": "Paluszki serowe z air fryera", "method": "air_fryer", "meal_type": "przekaska",
        "servings": 1, "calories": 260, "protein_g": 16, "fat_g": 18, "carbs_g": 10,
        "allergens": ["laktoza", "jaja", "gluten"],
        "ingredients": [
            {"name": "ser żółty", "quantity": 60, "unit": "g", "category": "nabial"},
            {"name": "jajko", "quantity": 1, "unit": "szt", "category": "nabial"},
            {"name": "mąka pszenna", "quantity": 20, "unit": "g", "category": "produkty sypkie"},
        ],
        "instructions": "1. Pokrój ser w słupki, obtocz w jajku i mące. 2. Piecz w air fryerze 190°C 8 min.",
    },
    {
        "id": 168, "name": "Koktajl bananowo-owsiany", "method": "tradycyjne", "meal_type": "przekaska",
        "servings": 1, "calories": 260, "protein_g": 9, "fat_g": 5, "carbs_g": 46,
        "allergens": ["laktoza", "gluten"],
        "ingredients": [
            {"name": "banan", "quantity": 1, "unit": "szt", "category": "owoce"},
            {"name": "mleko", "quantity": 200, "unit": "ml", "category": "nabial"},
            {"name": "płatki owsiane", "quantity": 20, "unit": "g", "category": "produkty sypkie"},
        ],
        "instructions": "1. Zmiksuj wszystkie składniki na gładko.",
    },
    {
        "id": 169, "name": "Sałatka owocowa", "method": "tradycyjne", "meal_type": "przekaska",
        "servings": 1, "calories": 130, "protein_g": 1, "fat_g": 0, "carbs_g": 32,
        "allergens": [],
        "ingredients": [
            {"name": "jabłko", "quantity": 0.5, "unit": "szt", "category": "owoce"},
            {"name": "banan", "quantity": 0.5, "unit": "szt", "category": "owoce"},
            {"name": "winogrona", "quantity": 60, "unit": "g", "category": "owoce"},
            {"name": "pomarańcza", "quantity": 0.5, "unit": "szt", "category": "owoce"},
        ],
        "instructions": "1. Pokrój owoce w kostkę. 2. Wymieszaj w misce.",
    },
]

ALLERGEN_LABELS = {
    "gluten": "Gluten",
    "laktoza": "Laktoza (mleko)",
    "jaja": "Jaja",
    "orzechy": "Orzechy",
    "orzeszki_ziemne": "Orzeszki ziemne",
    "ryby": "Ryby",
    "skorupiaki": "Skorupiaki",
    "soja": "Soja",
    "seler": "Seler",
    "gorczyca": "Gorczyca",
    "sezam": "Sezam",
}

METHOD_LABELS = {
    "air_fryer": "Air fryer",
    "lidlomix": "Lidlomix (multicooker)",
    "tradycyjne": "Tradycyjne gotowanie",
}

MEAL_TYPE_LABELS = {
    "sniadanie": "Śniadanie",
    "obiad": "Obiad",
    "kolacja": "Kolacja",
    "przekaska": "Przekąska",
}
