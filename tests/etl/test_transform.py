import pandas as pd
import pytest
from shared.models import DimEducation, DimOccupation, DimCountry, DimWorkclass, FactPerson
from etl.transform import transform


@pytest.fixture
def raw_df():
    return pd.DataFrame({
        "age": [39, 50, 38],
        "workclass": ["State-gov", "Self-emp-not-inc", "Private"],
        "fnlwgt": [77516, 83311, 215646],
        "education": ["Bachelors", "Bachelors", "HS-grad"],
        "education_num": [13, 13, 9],
        "marital_status": ["Never-married", "Married-civ-spouse", "Divorced"],
        "occupation": ["Adm-clerical", "Exec-managerial", "Handlers-cleaners"],
        "relationship": ["Not-in-family", "Husband", "Not-in-family"],
        "race": ["White", "White", "White"],
        "sex": ["Male", "Male", "Male"],
        "capital_gain": [2174, 0, 0],
        "capital_loss": [0, 0, 0],
        "hours_per_week": [40, 13, 40],
        "native_country": ["United-States", "United-States", "United-States"],
        "income": ["<=50K", "<=50K", "<=50K"],
    })


def test_transform_returns_five_dataframes(raw_df):
    result = transform(raw_df)
    assert set(result.keys()) == {"fact_person", "dim_education", "dim_occupation", "dim_country", "dim_workclass"}


def test_dim_education_unique(raw_df):
    result = transform(raw_df)
    assert result["dim_education"]["education"].nunique() == result["dim_education"]["education"].count()


def test_fact_person_has_fk_columns(raw_df):
    result = transform(raw_df)
    fact = result["fact_person"]
    assert "education_id" in fact.columns
    assert "occupation_id" in fact.columns
    assert "country_id" in fact.columns
    assert "workclass_id" in fact.columns


def test_transform_replaces_question_marks():
    df = pd.DataFrame({
        "age": [25], "workclass": ["?"], "fnlwgt": [100000],
        "education": ["HS-grad"], "education_num": [9],
        "marital_status": ["Single"], "occupation": ["?"],
        "relationship": ["Own-child"], "race": ["White"],
        "sex": ["Male"], "capital_gain": [0], "capital_loss": [0],
        "hours_per_week": [40], "native_country": ["United-States"],
        "income": ["<=50K"],
    })
    result = transform(df)
    assert result["dim_workclass"]["workclass"].iloc[0] == "Unknown"
    assert result["dim_occupation"]["occupation"].iloc[0] == "Unknown"


def test_fact_person_income_values(raw_df):
    result = transform(raw_df)
    assert set(result["fact_person"]["income"].unique()).issubset({"<=50K", ">50K"})
