#!/usr/bin/python3
"""
This script prints all City objects from the database
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City


def get_cities():
    """
     database to print all Cities
    """

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    session = Session(engine)

    states_cities = session.query(State, City).join(City).all()

    for state, city in states_cities:
        print(f"{state.name}: ({state.id}) {city.name}")


    session.close()

if __name__ == "__main__":
    get_cities()
