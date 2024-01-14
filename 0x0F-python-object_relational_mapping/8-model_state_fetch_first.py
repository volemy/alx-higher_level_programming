#!/usr/bin/python3
"""
This script prints the first State object from the database using SQLAlchemy.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

def list_first_state():
    """
    Connects to the database and prints the first State object.
    """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                                                                       argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    session.close()

if __name__ == "__main__":
    list_first_state()
