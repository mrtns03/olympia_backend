from sqlmodel import SQLModel, Field


class Laender(SQLModel, table=True):
    __tablename__ = "l_laender"
    l_pk: int = Field(default=None, primary_key=True)
    l_bezeichnung: str = Field()