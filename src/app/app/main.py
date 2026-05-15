import os
import requests
import pandas as pd
import streamlit as st

API_URL = os.getenv("API_URL", "http://localhost:8000")

st.set_page_config(page_title="Census Explorer", layout="wide")

# Sidebar : santé API
with st.sidebar:
    st.title("Census Explorer")
    try:
        resp = requests.get(f"{API_URL}/health", timeout=3)
        health = resp.json()
        if health.get("status") == "ok":
            st.success(f"API : {health['db']}")
        else:
            st.error("API : erreur")
    except Exception:
        st.error("API inaccessible")
    st.markdown(f"[Swagger docs]({API_URL}/docs)")

# Onglets
tab_sql, tab_stats = st.tabs(["SQL Explorer", "Statistiques"])

# --- Onglet SQL ---
with tab_sql:
    st.header("Requête SQL libre")
    st.caption("Lecture seule — INSERT/UPDATE/DELETE/DROP interdits")

    default_sql = (
        "SELECT f.age, f.income, e.education, o.occupation\n"
        "FROM fact_person f\n"
        "JOIN dim_education e ON f.education_id = e.id\n"
        "JOIN dim_occupation o ON f.occupation_id = o.id\n"
        "LIMIT 10"
    )
    sql = st.text_area("SQL", value=default_sql, height=120)

    if st.button("Exécuter"):
        with st.spinner("Requête en cours..."):
            try:
                resp = requests.post(f"{API_URL}/query", json={"sql": sql}, timeout=10)
                if resp.status_code == 200:
                    data = resp.json()
                    df = pd.DataFrame(data["rows"], columns=data["columns"])
                    st.success(f"{len(df)} ligne(s) retournée(s)")
                    st.dataframe(df, use_container_width=True)
                else:
                    st.error(f"Erreur : {resp.json().get('detail', 'inconnue')}")
            except Exception as e:
                st.error(f"Impossible de contacter l'API : {e}")

# --- Onglet Stats ---
with tab_stats:
    st.header("Statistiques Census")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Distribution des revenus")
        try:
            data = requests.get(f"{API_URL}/stats/income", timeout=5).json()
            df_income = pd.DataFrame(list(data.items()), columns=["Revenu", "Nombre"])
            st.bar_chart(df_income.set_index("Revenu"))
        except Exception:
            st.warning("Données indisponibles")

    with col2:
        st.subheader("Âge moyen par catégorie")
        try:
            data = requests.get(f"{API_URL}/stats/age", timeout=5).json()
            df_age = pd.DataFrame([
                {"Revenu": k, "Âge moyen": v["avg"], "Min": v["min"], "Max": v["max"]}
                for k, v in data.items()
            ])
            st.dataframe(df_age, use_container_width=True)
        except Exception:
            st.warning("Données indisponibles")

    st.subheader("Top occupations par revenu")
    try:
        data = requests.get(f"{API_URL}/stats/occupation", timeout=5).json()
        df_occ = pd.DataFrame(data)
        st.dataframe(df_occ, use_container_width=True)
    except Exception:
        st.warning("Données indisponibles")
