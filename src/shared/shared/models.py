from typing import Optional
from sqlmodel import SQLModel, Field


class DimEducation(SQLModel, table=True):
    __tablename__ = "dim_education"
    id: Optional[int] = Field(default=None, primary_key=True)
    education: str = Field(index=True, unique=True)
    education_num: int


class DimOccupation(SQLModel, table=True):
    __tablename__ = "dim_occupation"
    id: Optional[int] = Field(default=None, primary_key=True)
    occupation: str = Field(index=True, unique=True)


class DimCountry(SQLModel, table=True):
    __tablename__ = "dim_country"
    id: Optional[int] = Field(default=None, primary_key=True)
    native_country: str = Field(index=True, unique=True)


class DimWorkclass(SQLModel, table=True):
    __tablename__ = "dim_workclass"
    id: Optional[int] = Field(default=None, primary_key=True)
    workclass: str = Field(index=True, unique=True)


class FactPerson(SQLModel, table=True):
    __tablename__ = "fact_person"
    id: Optional[int] = Field(default=None, primary_key=True)
    age: int
    capital_gain: int
    capital_loss: int
    hours_per_week: int
    income: str  # "<=50K" or ">50K"
    education_id: Optional[int] = Field(default=None, foreign_key="dim_education.id")
    occupation_id: Optional[int] = Field(default=None, foreign_key="dim_occupation.id")
    country_id: Optional[int] = Field(default=None, foreign_key="dim_country.id")
    workclass_id: Optional[int] = Field(default=None, foreign_key="dim_workclass.id")
