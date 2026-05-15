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
        session.add_all([
            DimEducation(id=1, education="Bachelors", education_num=13),
            DimOccupation(id=1, occupation="Tech-support"),
            DimCountry(id=1, native_country="United-States"),
            DimWorkclass(id=1, workclass="Private"),
        ])
        session.add(FactPerson(age=35, capital_gain=0, capital_loss=0,
                                hours_per_week=40, income="<=50K",
                                education_id=1, occupation_id=1,
                                country_id=1, workclass_id=1))
        session.commit()
    return TestClient(create_app(db_path=str(db_path)))


def test_query_select_returns_results(client):
    response = client.post("/query", json={"sql": "SELECT * FROM fact_person"})
    assert response.status_code == 200
    data = response.json()
    assert "columns" in data
    assert "rows" in data
    assert len(data["rows"]) == 1


def test_query_columns_present(client):
    response = client.post("/query", json={"sql": "SELECT age, income FROM fact_person"})
    assert response.json()["columns"] == ["age", "income"]


def test_query_rejects_insert(client):
    response = client.post("/query", json={"sql": "INSERT INTO fact_person VALUES (1,2,3,4,'x',1,1,1,1)"})
    assert response.status_code == 400


def test_query_rejects_drop(client):
    response = client.post("/query", json={"sql": "DROP TABLE fact_person"})
    assert response.status_code == 400


def test_query_rejects_delete(client):
    response = client.post("/query", json={"sql": "DELETE FROM fact_person"})
    assert response.status_code == 400


def test_query_invalid_sql_returns_400(client):
    response = client.post("/query", json={"sql": "SELECT * FROM table_inexistante"})
    assert response.status_code == 400
