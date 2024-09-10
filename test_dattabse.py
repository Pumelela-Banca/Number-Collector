"""
Tests  for the database module
"""
import sqlite3


conn = sqlite3.connect('db.sqlite3')


# Create a cursor object
cursor = conn.cursor()

# Execute the query to list tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")

# Fetch all results
tables = cursor.fetchall()
# find items on teble lotto_api_lottop1
cursor.execute("SELECT * FROM lotto_api_lottop1")
# Fetch all results
items = cursor.fetchall()
for item in items:
    print('space')
    print(item)

# Print the table names
for table in tables:
    print(table[0])

# Close the connection
conn.close()
