#!/usr/bin/python3
"""Script to list all states by id in ASC"""

import sys
import MySQLdb


db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                     passwd=sys.argv[2],db=sys.argv[3])

cursor = db.cursor()
cursor.execute("SELECT * FROM states ORDER BY id ASC")
query_rows = cursor.fetchall()
for row in query_rows:
    print(row)
cursor.close()
db.close()
