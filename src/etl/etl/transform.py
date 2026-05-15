import pandas as pd
from typing import Dict


def transform(df: pd.DataFrame) -> Dict[str, pd.DataFrame]:
    df = df.copy()

    # Nettoyage : remplace '?' par 'Unknown' (pandas 2: object dtype, pandas 3: str dtype)
    str_cols = [c for c in df.columns if str(df[c].dtype) in ("object", "str", "string")]
    for col in str_cols:
        df[col] = df[col].str.strip().replace("?", "Unknown")

    # Normalise income (supprime le point final dans adult.test)
    df["income"] = df["income"].str.replace(".", "", regex=False)

    # Tables de dimension (valeurs uniques)
    dim_education = (
        df[["education", "education_num"]]
        .drop_duplicates(subset=["education"])
        .reset_index(drop=True)
    )
    dim_education.index += 1
    dim_education.index.name = "id"
    dim_education = dim_education.reset_index()

    dim_occupation = (
        df[["occupation"]].drop_duplicates().reset_index(drop=True)
    )
    dim_occupation.index += 1
    dim_occupation.index.name = "id"
    dim_occupation = dim_occupation.reset_index()

    dim_country = (
        df[["native_country"]].drop_duplicates().reset_index(drop=True)
    )
    dim_country.index += 1
    dim_country.index.name = "id"
    dim_country = dim_country.reset_index()

    dim_workclass = (
        df[["workclass"]].drop_duplicates().reset_index(drop=True)
    )
    dim_workclass.index += 1
    dim_workclass.index.name = "id"
    dim_workclass = dim_workclass.reset_index()

    # Mapping valeur → id
    edu_map = dim_education.set_index("education")["id"]
    occ_map = dim_occupation.set_index("occupation")["id"]
    country_map = dim_country.set_index("native_country")["id"]
    wc_map = dim_workclass.set_index("workclass")["id"]

    # Table de faits
    fact_person = pd.DataFrame({
        "age": df["age"],
        "capital_gain": df["capital_gain"],
        "capital_loss": df["capital_loss"],
        "hours_per_week": df["hours_per_week"],
        "income": df["income"],
        "education_id": df["education"].map(edu_map),
        "occupation_id": df["occupation"].map(occ_map),
        "country_id": df["native_country"].map(country_map),
        "workclass_id": df["workclass"].map(wc_map),
    })

    print(f"[TRANSFORM] ✓ 5 tables générées — {len(fact_person)} personnes")

    return {
        "fact_person": fact_person,
        "dim_education": dim_education,
        "dim_occupation": dim_occupation,
        "dim_country": dim_country,
        "dim_workclass": dim_workclass,
    }
