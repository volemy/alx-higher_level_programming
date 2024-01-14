#!/usr/bin/python3
"""
A script that retrieves and print a list of states whose names
matches argument provided, sorted in ascending order by states.id
"""
import MySQLdb
from sys import argv


def get_states_arg():
    """
    This retrieves and prints a list of states
    whose names match the provided argument, sorted by states.id
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE '{:s}'\
                    ORDER BY id ASC".format(argv[4]))

    rows = cursor.fetchall()
    for i in rows:
        print(i)

    cursor.close()
    db.close()


if __name__ == "__main__":
    get_states_arg()
