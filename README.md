# Data Engineering & SQL — Masterclass Liora

Démo complète pour une masterclass de 2h destinée aux data scientists juniors en fin de formation. Le projet illustre le travail d'un Data Engineer : ingestion, ETL, stockage, exposition des données.

## Architecture

```
CSV (UCI Adult) ──► ETL local ──► SQLite ──► API FastAPI ──► Streamlit
                   (terminal)    (disque)    (container)    (container)
```

**Schéma en étoile :**

| Table | Rôle |
|---|---|
| `fact_person` | 32 000+ individus avec revenus, âge, capital |
| `dim_education` | Niveaux d'éducation |
| `dim_occupation` | Catégories de métiers |
| `dim_country` | Pays d'origine |
| `dim_workclass` | Secteurs d'activité |

**Stack :** Python 3.12 · uv workspace · SQLModel · pandas · FastAPI · Streamlit · Docker Compose

## Prérequis

- [uv](https://docs.astral.sh/uv/) — gestionnaire de packages Python
- Docker & Docker Compose

## Démarrage rapide

```bash
# 1. Installer les dépendances
uv sync

# 2. Lancer le pipeline ETL (télécharge le dataset + charge SQLite)
uv run --package etl python -m etl.main

# 3. Lancer l'API + Streamlit via Docker
docker compose up --build
```

- API : http://localhost:8000
- Swagger : http://localhost:8000/docs
- Streamlit : http://localhost:8501

## Structure du projet

```
.
├── src/
│   ├── shared/        # Modèles SQLModel (partagés ETL ↔ API)
│   ├── etl/           # Pipeline Extract → Transform → Load
│   ├── api/           # FastAPI (stats + SQL libre)
│   └── app/           # Streamlit SQL Explorer
├── tests/
│   ├── etl/
│   └── api/
├── db/                # SQLite sur disque (gitignored sauf .gitkeep)
├── data/              # CSV brut (gitignored)
├── slides/            # Slides Marp de la masterclass
└── docker-compose.yml
```

## ETL

```bash
uv run --package etl python -m etl.main
```

```
==================================================
  Census ETL Pipeline
==================================================
[EXTRACT] Téléchargement du dataset UCI Adult...
[EXTRACT] ✓ 32561 lignes téléchargées → data/adult.csv
[TRANSFORM] ✓ 5 tables générées — 32561 personnes
[LOAD] ✓ db/census.db chargée — 32561 personnes
==================================================
  Pipeline terminée avec succès !
==================================================
```

L'ETL est **idempotent** : relancer efface et recharge proprement la base.

## API

| Endpoint | Description |
|---|---|
| `GET /health` | Santé de l'API et connexion DB |
| `GET /stats/income` | Distribution `<=50K` / `>50K` |
| `GET /stats/age` | Min / max / moyenne par tranche de revenu |
| `GET /stats/occupation` | Top occupations par revenu |
| `POST /query` | SQL libre (lecture seule) |

L'endpoint `/query` rejette tout `INSERT`, `UPDATE`, `DELETE`, `DROP`, `ALTER`, `CREATE`, `TRUNCATE`.

```bash
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"sql": "SELECT education, COUNT(*) as n FROM dim_education JOIN fact_person ON dim_education.id = fact_person.education_id GROUP BY education ORDER BY n DESC"}'
```

## Tests

```bash
uv run pytest tests/ -v
# 25 passed
```

## Slides

Les slides Marp sont dans `slides/data-engineering-sql.md`. Déploiement automatique sur GitHub Pages via `.github/workflows/deploy-slides.yml` à chaque push sur `main`.

Générer en local :

```bash
npx @marp-team/marp-cli slides/data-engineering-sql.md --html --allow-local-files -o slides/out/index.html
```

## Dataset

[UCI Adult / Census Income](https://archive.ics.uci.edu/dataset/2/adult) — 32 561 individus, 15 variables socio-démographiques, tâche de classification binaire (revenu `>50K` ou `<=50K`).
