from sqlmodel import SQLModel, Relationship, Field


class Ergebnisse(SQLModel, table=True):
    e_pk: int = Field(primary_key=True)
    e_a_pk: int = Field(foreign_key="athleten.a_pk")
    e_platzierung: int = Field()
    e_wert: int = Field()

    # Define the relationship with the Athleten table
    athleten: "Athleten" = Relationship(back_populates="ergebnisse")

    # Athleten.ergebnisse = Relationship(
    #     back_populates="athleten",
    #     sa_relationship_kwargs={
    #         "lazy": "selectin",
    #         "uselist": True,
    #     }
    # )
    #
    # Ergebnisse.e_a_pk.referenced_table = Athleten

# ergebnisse = session.exec(select(Ergebnisse, Athleten).join(Athleten)).all()