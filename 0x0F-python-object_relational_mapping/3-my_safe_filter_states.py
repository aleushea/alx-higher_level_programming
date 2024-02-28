#!/usr/bin/python3
"""
This script lists all states from the database hbtn with a given name
and is safe from MySQL injections.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Retrieve command-line arguments
    The_username = argv[1]
    The_password = argv[2]
    database_name = argv[3]
    state_name = argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=The_username,
                         passwd=The_password, db=database_name, charset="utf8")
    cursor = db.cursor()

    # Construct the SQL query using a placeholder
    sql_query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"

    # Execute the SQL query with the state name as a parameter
    cursor.execute(sql_query, (state_name,))

    # Fetch all the matching rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
