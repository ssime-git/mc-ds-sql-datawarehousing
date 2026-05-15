import pytest
from fastapi.testclient import TestClient
from sqlmodel import create_engine, SQLModel as SM
from api.main import create_app


@pytest.fixture
def client(tmp_path):
    db_path = tmp_path / "test.db"
    engine = create_engine(f"sqlite:///{db_path}")
    SM.metadata.create_all(engine)
    app = create_app(db_path=str(db_path))
    return TestClient(app)


def test_health_returns_ok(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_health_returns_db_connected(client):
    response = client.get("/health")
    assert response.json()["db"] == "connected"
