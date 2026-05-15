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
make install   # installe les dépendances
make etl       # télécharge le dataset et charge SQLite
make up        # lance API + Streamlit via Docker
```

Autres commandes utiles :

```bash
make test      # 25 tests pytest
make slides    # génère les slides en HTML local
make reset     # repart de zéro (containers, DB, venv)
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
make etl
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

## Schéma SQL

### Modèle en étoile

```
              dim_education
              (id, education, education_num)
                      │
dim_workclass ────────┤
(id, workclass)       │
                 fact_person
                 (id, age, capital_gain,
dim_occupation ──capital_loss, hours_per_week,
(id, occupation) income, education_id,
                  occupation_id, country_id,
dim_country ─────workclass_id)
(id, native_country)
```

`fact_person` est la table centrale. Chaque ligne est un individu. Les clés étrangères (`*_id`) pointent vers les dimensions.

### Explorer les tables

```sql
-- Voir la structure de la table de faits
SELECT * FROM fact_person LIMIT 5;

-- Voir les valeurs possibles d'une dimension
SELECT * FROM dim_education ORDER BY education_num DESC;
SELECT * FROM dim_occupation ORDER BY occupation;
SELECT * FROM dim_workclass;
SELECT * FROM dim_country ORDER BY native_country;

-- Compter les lignes dans chaque table
SELECT 'fact_person'   AS tbl, COUNT(*) AS n FROM fact_person
UNION ALL
SELECT 'dim_education',         COUNT(*) FROM dim_education
UNION ALL
SELECT 'dim_occupation',        COUNT(*) FROM dim_occupation
UNION ALL
SELECT 'dim_country',           COUNT(*) FROM dim_country
UNION ALL
SELECT 'dim_workclass',         COUNT(*) FROM dim_workclass;
```

### Comprendre les jointures

```sql
-- Reconstituer un profil lisible (dénormalisation)
SELECT
    f.age,
    f.hours_per_week,
    f.capital_gain,
    f.income,
    e.education,
    e.education_num,
    o.occupation,
    w.workclass,
    c.native_country
FROM fact_person f
JOIN dim_education  e ON f.education_id  = e.id
JOIN dim_occupation o ON f.occupation_id = o.id
JOIN dim_workclass  w ON f.workclass_id  = w.id
JOIN dim_country    c ON f.country_id    = c.id
LIMIT 10;
```

### Questions business et requêtes associées

**Quelle est la distribution des revenus ?**
```sql
SELECT income, COUNT(*) AS n,
       ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 1) AS pct
FROM fact_person
GROUP BY income;
```

**Quels niveaux d'éducation mènent le plus souvent à un revenu >50K ?**
```sql
SELECT
    e.education,
    e.education_num,
    COUNT(*) FILTER (WHERE f.income = '>50K')  AS n_high,
    COUNT(*)                                    AS n_total,
    ROUND(COUNT(*) FILTER (WHERE f.income = '>50K') * 100.0 / COUNT(*), 1) AS pct_high
FROM fact_person f
JOIN dim_education e ON f.education_id = e.id
GROUP BY e.education, e.education_num
ORDER BY e.education_num DESC;
```

**Quels secteurs d'activité concentrent les hauts revenus ?**
```sql
SELECT
    w.workclass,
    COUNT(*) FILTER (WHERE f.income = '>50K')  AS n_high,
    COUNT(*)                                    AS n_total,
    ROUND(COUNT(*) FILTER (WHERE f.income = '>50K') * 100.0 / COUNT(*), 1) AS pct_high
FROM fact_person f
JOIN dim_workclass w ON f.workclass_id = w.id
GROUP BY w.workclass
ORDER BY pct_high DESC;
```

**Les heures travaillées influencent-elles le revenu ?**
```sql
SELECT
    income,
    MIN(hours_per_week)                    AS min_h,
    MAX(hours_per_week)                    AS max_h,
    ROUND(AVG(hours_per_week), 1)          AS avg_h,
    ROUND(AVG(capital_gain), 0)            AS avg_capital_gain
FROM fact_person
GROUP BY income;
```

**Top 10 des métiers les mieux rémunérés (taux >50K) ?**
```sql
SELECT
    o.occupation,
    COUNT(*)                                                        AS n_total,
    ROUND(COUNT(*) FILTER (WHERE f.income = '>50K') * 100.0 / COUNT(*), 1) AS pct_high
FROM fact_person f
JOIN dim_occupation o ON f.occupation_id = o.id
GROUP BY o.occupation
HAVING COUNT(*) > 100
ORDER BY pct_high DESC
LIMIT 10;
```

**Profil moyen par pays d'origine (top 10 pays) ?**
```sql
SELECT
    c.native_country,
    COUNT(*)                               AS n,
    ROUND(AVG(f.age), 1)                   AS avg_age,
    ROUND(AVG(f.hours_per_week), 1)        AS avg_hours,
    ROUND(COUNT(*) FILTER (WHERE f.income = '>50K') * 100.0 / COUNT(*), 1) AS pct_high
FROM fact_person f
JOIN dim_country c ON f.country_id = c.id
GROUP BY c.native_country
ORDER BY n DESC
LIMIT 10;
```

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
make test
# 25 passed
```

## Slides

Les slides Marp sont dans `slides/data-engineering-sql.md`. Déploiement automatique sur GitHub Pages via `.github/workflows/deploy-slides.yml` à chaque push sur `main`.

Générer en local : `make slides`

## Dataset

[UCI Adult / Census Income](https://archive.ics.uci.edu/dataset/2/adult) — 32 561 individus, 15 variables socio-démographiques, tâche de classification binaire (revenu `>50K` ou `<=50K`).
