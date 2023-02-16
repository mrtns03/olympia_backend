from pydantic import Field
from sqlmodel import SQLModel


class Laender(SQLModel, table=True):
    l_pk: int = Field(primary_key=True)
    l_bezeichnung: str = Field(sa_column_name="l_bezeichnung")