from sqlmodel import select

from models.Athlethen import Athleten
from models.Ergebnisse import Ergebnisse


def select_ergebnisse(session):
    return session.execute(select(Ergebnisse, Athleten).join(Athleten)).all()
