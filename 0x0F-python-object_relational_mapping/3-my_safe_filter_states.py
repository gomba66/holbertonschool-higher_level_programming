#!/usr/bin/python3
""" Import the sys.arg """
import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states\
    WHERE name LIKE %s ORDER BY id ASC;", (sys.argv[4],))

    tables = cursor.fetchall()

    for column in tables:
        print(column)

    cursor.close()
    db.close()
