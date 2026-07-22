# Dieta App

Prosta aplikacja webowa (Flask + Docker) do planowania diety odchudzającej:

- własna baza ~55 przepisów (air fryer, Lidlomix/multicooker, tradycyjne gotowanie),
- wyliczanie dziennego zapotrzebowania kalorycznego pod utratę wagi (na podstawie wagi, wzrostu, wieku, aktywności i tempa chudnięcia),
- automatyczne wykluczanie przepisów zawierających wskazane alergeny (gluten, laktoza, orzechy, ryby itd.)
  **oraz dowolny konkretny, wskazany przez siebie składnik** (np. ogórek) spoza standardowej listy alergenów,
- generowanie jadłospisu na wybrany okres (7 dni / 30 dni / 90 dni - 3 miesiące) dopasowanego do celu kalorycznego,
- lista zakupów zsumowana ze wszystkich przepisów z jadłospisu,
- śledzenie postępów odchudzania: historia pomiarów wagi, wykres, pasek postępu do wagi docelowej.

Dane profilu (waga, cel, alergie, wykluczone składniki), historia wagi i bieżący jadłospis zapisywane są lokalnie
w plikach JSON w katalogu `data/` (jeden profil - bez logowania, do użytku jednoosobowego).

## Uruchomienie lokalne (Docker)

Wymagany zainstalowany Docker Desktop.

```bash
docker compose up --build
```

Aplikacja będzie dostępna pod adresem: http://localhost:5000

Dane profilu i jadłospisu przetrwają restart kontenera (zapisywane w `./data`, montowane jako wolumen).

## Uruchomienie bez Dockera (do szybkich testów)

```bash
pip install -r requirements.txt
python main.py
```

## Udostępnienie aplikacji przez link (hosting)

Docker uruchomiony lokalnie działa tylko na Twoim komputerze. Żeby wysłać komuś link, aplikację trzeba wystawić
na hostingu w internecie. Poniżej najprostsza, tania/darmowa opcja - **Fly.io** (obsługuje bezpośrednio Twój
Dockerfile i oferuje trwały dysk na dane profilu).

### Wdrożenie na Fly.io

1. Załóż konto na https://fly.io i zainstaluj narzędzie `flyctl` (instrukcje na stronie Fly.io dla Twojego systemu).
2. Zaloguj się: `fly auth login`
3. W katalogu `dieta-app` uruchom: `fly launch` (Fly wykryje Dockerfile, zapyta o nazwę aplikacji i region -
   wybierz np. `waw` - Warszawa). Na pytanie o bazę danych/Redis odpowiedz "nie" (aplikacja jej nie potrzebuje).
4. Dodaj trwały wolumen na dane profilu:
   ```bash
   fly volumes create dieta_data --size 1 --region waw
   ```
   i w wygenerowanym pliku `fly.toml` dodaj sekcję:
   ```toml
   [mounts]
     source = "dieta_data"
     destination = "/app/data"
   ```
5. Wdróż: `fly deploy`
6. Po chwili Fly.io wyświetli publiczny adres (np. `https://twoja-aplikacja.fly.dev`) - to jest link, który możesz
   przesłać innej osobie.

### Alternatywa: Railway.app

Jeśli wolisz prostszy interfejs graniczny bez terminala: załóż konto na https://railway.app, wybierz
"Deploy from GitHub repo" (repo z tym projektem), Railway samo wykryje Dockerfile. W ustawieniach usługi dodaj
"Volume" zamontowany w `/app/data`, żeby dane profilu przetrwały restarty.

## Struktura projektu

```
dieta-app/
  app/
    recipes_data.py   - baza przepisow (dane statyczne)
    calorie.py         - wyliczanie BMR/CPM i celu kalorycznego
    planner.py          - generator jadlospisu na 7 dni + lista zakupow
    storage.py           - zapis/odczyt profilu i jadlospisu (pliki JSON)
    routes.py             - endpointy Flask
    templates/              - widoki HTML
    static/style.css        - style
  main.py               - punkt wejscia aplikacji
  Dockerfile, docker-compose.yml, requirements.txt
  data/                  - tu zapisuja sie dane profilu (tworzone automatycznie)
```

## Rozbudowa bazy przepisów

Nowe przepisy dodaje się w `app/recipes_data.py`, w liście `RECIPES` - każdy jako słownik z polami
`method`, `meal_type`, `calories`/`protein_g`/`fat_g`/`carbs_g`, `allergens` i `ingredients`
(każdy składnik z `name`, `quantity`, `unit`, `category`).
