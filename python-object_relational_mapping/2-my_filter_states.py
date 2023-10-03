#!/usr/bin/python3
"""Takes an argument and displays all values in the states table of hbtn
"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
                 ORDER BY states.id ASC".format(sys.argv[4]))
    rows = cur.fetchall()
    for r in rows:
        print(r)
