#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Retrieve command-line arguments
    The_username = argv[1]
    The_password = argv[2]
    DB_name = argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=The_username,
                         passwd=The_password, db=DB_name, charset="utf8")
    cursor = db.cursor()

    # Execute the SQL query to fetch cities with associated state names
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
                    JOIN states ON cities.state_id = states.id ORDER BY \
                    cities.id")

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
