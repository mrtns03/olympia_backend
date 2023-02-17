from sqlmodel import select, Session, create_engine

from models.Athlethen import Athleten
from models.Ergebnisse import Ergebnisse
from models.Laender import Laender
from models.Sportarten import Sportarten
from models.login_models import User

engine = create_engine("sqlite:///new_olympia.db")


def get_user(username: str):
    with Session(engine) as session:
        result = session.execute(f"SELECT id, username, hashed_password FROM users WHERE username = '{username}'").one()
        if result is None:
            return None
        user = User(id=result[0], username=result[1], hashed_password=result[2])
        return user


def insert_user(username: str, hashed_password: str):
    with Session(engine) as session:
        session.execute("INSERT INTO users (username, hashed_password) VALUES (?, ?)", (username, hashed_password))
        session.commit()


def select_ergebnisse():
    with Session(engine) as session:
        return session.execute(select(Ergebnisse, Athleten).join(Athleten)).all()


def select_athletes():
    with Session(engine) as session:
        return session.execute(
            select(Athleten, Laender, Sportarten)
            .join(Laender, Laender.l_pk == Athleten.a_l_pk)
            .join(Sportarten, Sportarten.s_pk == Athleten.a_s_pk)
        ).all()


def select_athletes_by_nation(nation: str):
    with Session(engine) as session:
        return session.execute(
            select(Athleten, Laender, Sportarten)
            .join(Laender, Laender.l_pk == Athleten.a_l_pk)
            .join(Sportarten, Sportarten.s_pk == Athleten.a_s_pk)
            .where(Laender.l_bezeichnung == nation)
        ).all()
