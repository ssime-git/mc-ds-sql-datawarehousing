import pandas as pd
from pathlib import Path
from typing import Dict
from sqlmodel import SQLModel, create_engine, Session
from shared.models import DimEducation, DimOccupation, DimCountry, DimWorkclass, FactPerson


def load(tables: Dict[str, pd.DataFrame], db_path: Path = Path("db/census.db")) -> None:
    db_path = Path(db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)

    engine = create_engine(f"sqlite:///{db_path}")
    SQLModel.metadata.drop_all(engine)   # idempotent : recrée proprement
    SQLModel.metadata.create_all(engine)

    model_map = {
        "dim_education": DimEducation,
        "dim_occupation": DimOccupation,
        "dim_country": DimCountry,
        "dim_workclass": DimWorkclass,
        "fact_person": FactPerson,
    }

    # Dims d'abord, fact ensuite (contraintes FK)
    order = ["dim_education", "dim_occupation", "dim_country", "dim_workclass", "fact_person"]

    with Session(engine) as session:
        for table_name in order:
            df = tables[table_name]
            model_cls = model_map[table_name]
            records = [model_cls(**row) for row in df.to_dict(orient="records")]
            session.add_all(records)
        session.commit()

    total = len(tables["fact_person"])
    print(f"[LOAD] ✓ {db_path} chargée — {total} personnes")
