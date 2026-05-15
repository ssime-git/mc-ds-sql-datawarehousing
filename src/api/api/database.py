from sqlmodel import create_engine, Session, SQLModel
from shared.models import DimEducation, DimOccupation, DimCountry, DimWorkclass, FactPerson

_engine = None


def init_db(db_path: str) -> None:
    global _engine
    _engine = create_engine(f"sqlite:///{db_path}", connect_args={"check_same_thread": False})


def get_engine():
    if _engine is None:
        raise RuntimeError("DB non initialisée. Appeler init_db() d'abord.")
    return _engine


def get_session():
    with Session(get_engine()) as session:
        yield session
