#!/usr/bin/python3
"""Takes in arguments and displays all values in the states table
"""

import sys
import MySQLdb


if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])


    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name =%s\
                  ORDER BY states.id ASC", (sys.argv[4],))
    
    rows = cur.fetchall()
    
    for r in rows:
        print(r)