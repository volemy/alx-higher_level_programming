#!/usr/bin/python3
"""
A script that retrieves and prints a list of states whose names
match provided argument sorted in ascending order by states.id
"""
import MySQLdb
from sys import argv

def get_states_no_injectn():
    """
    This retrieves and print a list of states whose names
    match the provided argument, sorted by states.id
    """
    db = MySQLdb.connect(host="localhost",
                        port=3306,
                        user=argv[1],
                        passwd=argv[2],
                        db=argv[3])

    cursor = db.cursor()


    query = "SELECT * FROM states WHERE name LIKE %s ORDER by id ASC"
    cursor.execute(query, (argv[4],))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()

if __name__ == "__main__":
    get_states_no_injectn()
