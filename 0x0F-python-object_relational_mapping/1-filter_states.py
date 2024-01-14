#!/usr/bin/python3
"""
A script that lists states whose names start with the letter 'N'
(upper N), from database sorted in ascending order by states.id
"""
import MySQLdb
from sys import argv


def get_n_states():
    """
    This prints a list of states
    whose names start with the letter 'N', sorted by states.id
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY\
                     'N%' ORDER BY id")

    rows = cursor.fetchall()
    for i in rows:
        print(i)

    cursor.close()
    db.close()


if __name__ == "__main__":
    get_n_states()
