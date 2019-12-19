#!/usr/bin/python3
""" Import the sys.arg """
import MySQLdb
import sys

if __name__ == "__main__":
    # Database Conection
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    cur = db.cursor()

    # Execute the query and return to the cursor also prevent sql inj
    cur.execute("SELECT cities.name FROM cities LEFT JOIN states\
    ON states.id = cities.state_id WHERE states.name = %s\
    ORDER BY cities.id ASC;", (sys.argv[4],))

    query = cur.fetchall()
    list_a = []
    for element in query:
        list_a.append(element[0])
    result = ", ".join(list_a)
    print(result)

    cur.close()
    db.close()
