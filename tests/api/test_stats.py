import pytest
from fastapi.testclient import TestClient
from sqlmodel import create_engine, Session, SQLModel as SM
from shared.models import DimEducation, DimOccupation, DimCountry, DimWorkclass, FactPerson
from api.main import create_app


@pytest.fixture
def client(tmp_path):
    db_path = tmp_path / "test.db"
    engine = create_engine(f"sqlite:///{db_path}")
    SM.metadata.create_all(engine)

    with Session(engine) as session:
        edu = DimEducation(id=1, education="Bachelors", education_num=13)
        occ = DimOccupation(id=1, occupation="Adm-clerical")
        country = DimCountry(id=1, native_country="United-States")
        wc = DimWorkclass(id=1, workclass="Private")
        session.add_all([edu, occ, country, wc])
        session.add(FactPerson(age=30, capital_gain=0, capital_loss=0, hours_per_week=40,
                                income="<=50K", education_id=1, occupation_id=1,
                                country_id=1, workclass_id=1))
        session.add(FactPerson(age=45, capital_gain=5000, capital_loss=0, hours_per_week=50,
                                income=">50K", education_id=1, occupation_id=1,
                                country_id=1, workclass_id=1))
        session.commit()

    app = create_app(db_path=str(db_path))
    return TestClient(app)


def test_stats_income_returns_two_categories(client):
    response = client.get("/stats/income")
    assert response.status_code == 200
    data = response.json()
    assert "<=50K" in data
    assert ">50K" in data


def test_stats_income_counts(client):
    response = client.get("/stats/income")
    data = response.json()
    assert data["<=50K"] == 1
    assert data[">50K"] == 1


def test_stats_age_structure(client):
    response = client.get("/stats/age")
    assert response.status_code == 200
    data = response.json()
    assert "<=50K" in data
    for category in data.values():
        assert "min" in category
        assert "max" in category
        assert "avg" in category


def test_stats_occupation_structure(client):
    response = client.get("/stats/occupation")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert "occupation" in data[0]
    assert "income" in data[0]
    assert "count" in data[0]
