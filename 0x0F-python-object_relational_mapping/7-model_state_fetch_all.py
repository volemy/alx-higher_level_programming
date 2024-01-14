#!/usr/bin/python3
"""
This Lists all states from the database using SQLAlchemy
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


def list_all_states():
    """
    This Connect to the database and list all states
    """
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                                                                       argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)


    rows = session.query(State).order_by(state.id).all()

    for row in rows:
        print(f"{row.id}: {row.name}")

    session.close()


if __name__ == "__main__":
    list_all_states()
