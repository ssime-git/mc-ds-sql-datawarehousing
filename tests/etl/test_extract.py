import pandas as pd
import pytest
from pathlib import Path
from etl.extract import extract


def test_extract_returns_dataframe(tmp_path):
    df = extract(output_dir=tmp_path)
    assert isinstance(df, pd.DataFrame)


def test_extract_has_expected_columns(tmp_path):
    df = extract(output_dir=tmp_path)
    expected = {
        "age", "workclass", "fnlwgt", "education", "education_num",
        "marital_status", "occupation", "relationship", "race", "sex",
        "capital_gain", "capital_loss", "hours_per_week", "native_country", "income"
    }
    assert expected.issubset(set(df.columns))


def test_extract_saves_csv(tmp_path):
    extract(output_dir=tmp_path)
    assert (tmp_path / "adult.csv").exists()


def test_extract_row_count(tmp_path):
    df = extract(output_dir=tmp_path)
    assert len(df) > 30000  # dataset complet ~48842 lignes
