from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Teams, Standings, base

uri = getenv("DATABASE_URL") or "sqlite:///test.db"
engine = create_engine(uri)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)()


def create_all():
    base.metadata.create_all(engine)


def insert_to_teams(data):
    for t in data:
        team = Teams(
            t["id"],
            t["teamName"],
            t["name"],
            t["abbreviation"],
            t["locationName"],
            t["league"]["id"],
            t["division"]["id"],
        )
        session.add(team)
    session.commit()


def insert_to_standings(data):
    for daily_record in data:
        for team in daily_record:
            standing = Standings(**team)
            session.add(standing)
    session.commit()
