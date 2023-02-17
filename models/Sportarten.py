from pydantic import Field
from sqlmodel import SQLModel


class Sportarten(SQLModel, table=True):
    __tablename__ = "s_sportarten"
    s_pk: int = Field(primary_key=True)
    s_name: str = Field(sa_column_name="s_name")