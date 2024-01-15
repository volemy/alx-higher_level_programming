#!/usr/bin/python3
"""
A script that lists all cities sorted by city ID
"""

import MySQLdb
from sys import argv


def list_cities():
    """
    This lists ciities from mentioned database sorted by city ID
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities"
               " JOIN states ON cities.state_id = states.id"
               " ORDER BY cities.id ASC")


    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_cities()
