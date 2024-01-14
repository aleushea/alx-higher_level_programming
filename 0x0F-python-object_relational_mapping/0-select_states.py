#!/usr/bin/python3
"""
this python script lists all states from the database
"""
import MySQLdb
from sys  import argv
if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.excute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    db.close()
