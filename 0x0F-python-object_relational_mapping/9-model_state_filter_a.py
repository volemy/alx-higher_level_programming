#!/usr/bin/python3
"""
This lists all states containing 'a' from the database using SQLAlchemy
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def state_filter():
    """
    This method prints states containing the letter 'a'
    """

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                                                                       argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()

if __name__ == "__main__":
    state_filter()
