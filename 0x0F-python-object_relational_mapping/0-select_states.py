#!/usr/bin/python3
"""
A script that lists all states from database specified,
sorted in ascending order by states.id.
"""
import MySQLdb
from sys import argv


def get_states():
    """
    Connect to the MySQL server,retrieve and print a list of states
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER  BY id ASC")
    rows = cursor.fetchall()
    for i in rows:
        print(i)

    cursor.close()
    db.close()


if __name__ == "__main__":

    get_states()
