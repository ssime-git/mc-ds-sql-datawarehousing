import os
from fastapi import FastAPI
from api.database import init_db
from api.routers import stats, query


def create_app(db_path: str | None = None) -> FastAPI:
    app = FastAPI(title="Census API", version="1.0.0")

    path = db_path or os.getenv("DB_PATH", "db/census.db")
    init_db(path)

    @app.get("/health")
    def health():
        try:
            from sqlmodel import text
            from api.database import get_engine
            with get_engine().connect() as conn:
                conn.execute(text("SELECT 1"))
            return {"status": "ok", "db": "connected"}
        except Exception:
            return {"status": "ok", "db": "error"}

    app.include_router(stats.router, prefix="/stats")
    app.include_router(query.router)

    return app


app = create_app()
