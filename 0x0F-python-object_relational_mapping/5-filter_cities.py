#!/usr/bin/python3
"""Script to list all states by id in ASC"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("""SELECT name FROM cities
    WHERE cities.state_id = (SELECT id FROM states
    WHERE name='{:s}')
    ORDER BY cities.id ASC;""".format(sys.argv[4]))
    cities = []
    for row in cur.fetchall():
        cities.append(row[0])
    printcities = ", ".join(cities)
    print(printcities)
    cur.close()
    db.close()
