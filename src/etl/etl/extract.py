import pandas as pd
import requests
from pathlib import Path

UCI_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"

COLUMNS = [
    "age", "workclass", "fnlwgt", "education", "education_num",
    "marital_status", "occupation", "relationship", "race", "sex",
    "capital_gain", "capital_loss", "hours_per_week", "native_country", "income",
]


def extract(output_dir: Path = Path("data")) -> pd.DataFrame:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    csv_path = output_dir / "adult.csv"

    print("[EXTRACT] Téléchargement du dataset UCI Adult...")
    response = requests.get(UCI_URL, timeout=30)
    response.raise_for_status()
    csv_path.write_bytes(response.content)

    df = pd.read_csv(csv_path, header=None, names=COLUMNS, skipinitialspace=True)
    print(f"[EXTRACT] ✓ {len(df)} lignes téléchargées → {csv_path}")
    return df
