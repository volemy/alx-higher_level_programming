#!/usr/bin/python3
"""
This Lists first state from the database using SQLAlchemy
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

def list_first_state():
    """
    This Connect to the database and list the first state
    """

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    first = session.query(State).first()

    if first:
        print("{first.id}: {first.name}")
    else:
        print("Nothing")


    session.close()

if __name__ == "__main__":
    list_first_state(
