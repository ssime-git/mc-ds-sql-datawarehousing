import pandas as pd
import pytest
from pathlib import Path
from sqlmodel import create_engine, Session, select
from shared.models import DimEducation, FactPerson, SQLModel
from etl.load import load


@pytest.fixture
def sample_tables():
    return {
        "dim_education": pd.DataFrame({"id": [1, 2], "education": ["Bachelors", "HS-grad"], "education_num": [13, 9]}),
        "dim_occupation": pd.DataFrame({"id": [1], "occupation": ["Adm-clerical"]}),
        "dim_country": pd.DataFrame({"id": [1], "native_country": ["United-States"]}),
        "dim_workclass": pd.DataFrame({"id": [1], "workclass": ["Private"]}),
        "fact_person": pd.DataFrame({
            "age": [39], "capital_gain": [0], "capital_loss": [0],
            "hours_per_week": [40], "income": ["<=50K"],
            "education_id": [1], "occupation_id": [1],
            "country_id": [1], "workclass_id": [1],
        }),
    }


def test_load_creates_tables(tmp_path, sample_tables):
    db_path = tmp_path / "test.db"
    load(sample_tables, db_path=db_path)
    assert db_path.exists()


def test_load_inserts_dim_education(tmp_path, sample_tables):
    db_path = tmp_path / "test.db"
    load(sample_tables, db_path=db_path)
    engine = create_engine(f"sqlite:///{db_path}")
    with Session(engine) as session:
        results = session.exec(select(DimEducation)).all()
    assert len(results) == 2


def test_load_inserts_fact_person(tmp_path, sample_tables):
    db_path = tmp_path / "test.db"
    load(sample_tables, db_path=db_path)
    engine = create_engine(f"sqlite:///{db_path}")
    with Session(engine) as session:
        results = session.exec(select(FactPerson)).all()
    assert len(results) == 1
    assert results[0].age == 39


def test_load_is_idempotent(tmp_path, sample_tables):
    db_path = tmp_path / "test.db"
    load(sample_tables, db_path=db_path)
    load(sample_tables, db_path=db_path)  # 2e appel
    engine = create_engine(f"sqlite:///{db_path}")
    with Session(engine) as session:
        results = session.exec(select(FactPerson)).all()
    assert len(results) == 1  # pas de doublon
