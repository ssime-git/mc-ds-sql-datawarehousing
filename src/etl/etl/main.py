from pathlib import Path
from etl.extract import extract
from etl.transform import transform
from etl.load import load


def main():
    print("=" * 50)
    print("  Census ETL Pipeline")
    print("=" * 50)

    df_raw = extract(output_dir=Path("data"))
    tables = transform(df_raw)
    load(tables, db_path=Path("db/census.db"))

    print("=" * 50)
    print("  Pipeline terminée avec succès !")
    print("=" * 50)


if __name__ == "__main__":
    main()
