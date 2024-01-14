#!/usr/bin/python3
"""
A script that retrieves and print a list of states whose names
matches argument provided, sorted in ascending order by states.id
"""
import MySQLdb
from sys import argv


def select_states_arg():
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

    cursor.execute(
            "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
            (argv[4],))

    row = cursor.fetchall()
    for i in row:
        print(i)

    cursor.close()
    db.close()


if __name__ == "__main__":
    select_states_arg()
