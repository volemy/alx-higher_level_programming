#!/usr/bin/python3
"""
This script adds the State object “Louisiana” to the database
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def add_state_obj():
    """
    this method adds a State object to the database
    """

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                                                                       argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    new_state = State(name='Louisiana')

    session.add(new_state)

    session.commit()
    print(new_state.id)

    session.close()


if __name__ == "__main__":
    add_state_obj()
