from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sqlalchemy import text
from api.database import get_engine

router = APIRouter(tags=["query"])

FORBIDDEN_KEYWORDS = {"insert", "update", "delete", "drop", "alter", "create", "truncate"}


class QueryRequest(BaseModel):
    sql: str


def is_safe(sql: str) -> bool:
    tokens = set(sql.lower().split())
    return not tokens.intersection(FORBIDDEN_KEYWORDS)


@router.post("/query")
def run_query(request: QueryRequest):
    if not is_safe(request.sql):
        raise HTTPException(status_code=400, detail="Requête non autorisée (écriture interdite).")
    try:
        with get_engine().connect() as conn:
            result = conn.execute(text(request.sql))
            columns = list(result.keys())
            rows = [list(row) for row in result.fetchall()]
        return {"columns": columns, "rows": rows}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
