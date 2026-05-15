from fastapi import APIRouter, Depends
from sqlmodel import Session, select, func
from api.database import get_session
from shared.models import FactPerson, DimOccupation

router = APIRouter(tags=["stats"])


@router.get("/income")
def stats_income(session: Session = Depends(get_session)):
    results = session.exec(
        select(FactPerson.income, func.count(FactPerson.id).label("count"))
        .group_by(FactPerson.income)
    ).all()
    return {row.income: row.count for row in results}


@router.get("/age")
def stats_age(session: Session = Depends(get_session)):
    results = session.exec(
        select(
            FactPerson.income,
            func.min(FactPerson.age).label("min"),
            func.max(FactPerson.age).label("max"),
            func.avg(FactPerson.age).label("avg"),
        ).group_by(FactPerson.income)
    ).all()
    return {
        row.income: {"min": row.min, "max": row.max, "avg": round(row.avg, 1)}
        for row in results
    }


@router.get("/occupation")
def stats_occupation(session: Session = Depends(get_session)):
    results = session.exec(
        select(
            DimOccupation.occupation,
            FactPerson.income,
            func.count(FactPerson.id).label("count"),
        )
        .join(FactPerson, FactPerson.occupation_id == DimOccupation.id)
        .group_by(DimOccupation.occupation, FactPerson.income)
        .order_by(func.count(FactPerson.id).desc())
        .limit(20)
    ).all()
    return [{"occupation": r.occupation, "income": r.income, "count": r.count} for r in results]
