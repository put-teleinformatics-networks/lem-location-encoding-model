# LEM — Location Encoding Model 1.0

Kandydat RC2 do preprintu typu **technical specification / research report**.

- Autor wskazany w manuskrypcie: mgr Piotr Augustyniak
- Jednostka: Politechnika Poznańska, Wydział Informatyki i Telekomunikacji
- Nr raportu: RP/01/2026 PL
- Data wersji: 2026-09-13
- Kompilator: pdfLaTeX + BibTeX

## Najważniejsze decyzje modelu 1.0

- LEM oznacza wyłącznie **Location Encoding Model**.
- Tekst ma od 1 do 256 punktów kodowych Unicode; limity oktetów należą do reprezentacji.
- `Level.value` jest liczbą całkowitą ze znakiem `int32`.
- Równoważność oznacza dokładną równość zdekodowanej krotki częściowej `(Site?, Building?, Level?, ReferenceSpace?, RelativePosition?)`.
- Model podstawowy nie odgaduje synonimów ani tożsamości nazw naturalnojęzykowych.
- DNS-safe jest stratnym aliasem prezentacyjnym, nie odwracalną reprezentacją LEM.
- Profil TLV używa T = 1 oktet, L = 2 oktety i 5-oktetowej wartości numerycznego `Level` (`kind` + `int32`).

## Struktura

```text
main.tex
bibliography.bib
chapters/                 rozdziały 1–8 i glosariusz
schemas/                  schemat podstawowy i dwa profile JSON Schema
yang/lem-location.yang    informacyjne mapowanie YANG
tests/                    20 wektorów pozytywnych i negatywnych
figures/                  logotypy wymagane przez klasę dokumentu
```

## Kompilacja

```bash
latexmk -pdf main.tex
```

Projekt jest przygotowany do importu w Overleaf jako ZIP. Plik główny to `main.tex`, a `latexmkrc` wybiera pdfLaTeX.

## Walidacja artefaktów

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r tests/requirements.txt
python tests/validate.py
pyang yang/lem-location.yang
```

## Trwałe identyfikatory i własność projektu

Wersja RC2 używa trwałej przestrzeni nazw `https://w3id.org/lem/`:

- specyfikacja LEM 1.0: `https://w3id.org/lem/1.0/specification`;
- podstawowy JSON Schema: `https://w3id.org/lem/1.0/schema/core`;
- profil emergency: `https://w3id.org/lem/1.0/profile/emergency`;
- profil network infrastructure: `https://w3id.org/lem/1.0/profile/network-infrastructure`;
- przestrzeń nazw YANG: `https://w3id.org/lem/yang/lem-location`.

Właścicielem i podmiotem utrzymującym repozytorium projektu, konfigurację przekierowań W3ID oraz wydania archiwalne jest **Politechnika Poznańska (Poznan University of Technology), Wydział Informatyki i Telekomunikacji (Faculty of Computing and Telecommunications), grupa badawcza pod kierunkiem Piotra Zwierzykowskiego**. Infrastruktura projektu nie należy do prywatnego konta autora ani kierownika zespołu. Techniczny identyfikator organizacji GitHub i docelowe adresy przekierowań należy wpisać podczas tworzenia repozytorium oraz rejestracji W3ID. Autorstwo raportu i prawa licencyjne pozostają odrębnymi kwestiami.

## Status naukowy

Wersja 1.0 jest specyfikacją techniczną z walidacją składniową artefaktów. Nie zawiera jeszcze eksperymentalnego porównania niezależnych implementacji; taki eksperyment jest rekomendowany jako podstawa późniejszego artykułu naukowego.

## Autorstwo i licencje

Jedynym autorem raportu jest **Piotr Augustyniak**. Piotr Zwierzykowski jest wskazany jako kierownik grupy badawczej i nie jest współautorem tej wersji. Wskazana wyżej jednostka i grupa badawcza są właścicielem infrastruktury projektu (repozytorium i konfiguracji trwałych identyfikatorów), lecz nie są przez to automatycznie autorem raportu ani właścicielem praw autorskich do jego treści.

- Treść raportu, źródła LaTeX oraz autorskie tabele i diagramy są udostępniane na licencji [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). Szczegóły i zalecany sposób atrybucji zawiera `LICENSE-DOCUMENTATION.md`.
- Schematy JSON, moduł YANG, kod walidacyjny i wektory testowe są udostępniane na licencji Apache License 2.0. Pełny tekst zawiera `LICENSE-CODE`, a informacje o zakresie — `NOTICE`.
- Powyższe licencje nie obejmują logotypów Politechniki Poznańskiej, znaków towarowych, klasy `ppfcmthesis.cls` ani materiałów osób trzecich. Elementy te podlegają prawom ich właścicieli.
