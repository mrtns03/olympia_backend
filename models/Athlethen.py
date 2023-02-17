from typing import Optional, Union

from sqlmodel import SQLModel, Relationship, Field


class Athleten(SQLModel, table=True):
    __tablename__ = "a_athleten"
    a_pk: Union[int, None] = Field(default=None, primary_key=True)
    a_name: str = Field()
    a_geburtsdatum: str = Field()
    a_l_pk: Union[int, None] = Field(default=None, foreign_key='l_länder.l_pk')
    a_e_pk: Union[int, None] = Field(default=None, foreign_key='e_ergebnisse.e_pk')
    a_s_pk: Union[int, None] = Field(default=None, foreign_key='s_sportarten.s_pk')
    #
    # e_ergebnisse: Optional["Ergebnisse"] = Relationship(back_populates="athleten")
    # l_laender: "Laender" = Relationship(back_populates="athleten")
    # s_sportarten: "Sportarten" = Relationship(back_populates="athleten")
