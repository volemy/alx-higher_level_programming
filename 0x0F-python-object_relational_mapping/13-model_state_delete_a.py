#!/usr/bin/python3
"""
This script deletes all State objects with a name containing
the letter a from the database
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def delete_state_a():
    """
    This method deletes states names containing 'a'
    """

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    states = session.query(State).all()

    for state in states:
        if 'a' in state.name:
            session.delete(state)

    session.commit()

    session.close()

if __name__ == "__main__":
    delete_state_a()
