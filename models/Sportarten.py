from sqlmodel import SQLModel, Field


class Sportarten(SQLModel, table=True):
    __tablename__ = "s_sportarten"
    s_pk: int = Field(primary_key=True)
    s_name: str = Field()