#!/usr/bin/python3
"""
A script to retrieve and print a list of cities
with their corresponding states
"""
import MySQLdb
from sys import argv


def list_cities_arg():
    """
    this retrieves and prints a list of cities
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT cities.name FROM cities\
                   JOIN states ON cities.state_id = states.id\
                   AND states.name = '{:s}'\
                   ORDER BY cities.id ASC".format(argv[4]))

    rows = cursor.fetchall()

    output = []

    for row in rows:
        output.append(row[0])

    print(", ".join(output))

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_cities_arg()
