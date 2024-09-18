"""
Tests  for the database module
"""
import sqlite3


conn = sqlite3.connect('db.sqlite3')


# Create a cursor object
cursor = conn.cursor()



# Execute the PRAGMA table_info command
cursor.execute("PRAGMA table_info(lotto_api_powerballp1)")

# Fetch all results
columns_info = cursor.fetchall()

# Extract column names
column_names = [info[1] for info in columns_info]

# Print column names
print("Column names:", column_names)
# Execute the query to list tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")

# # Fetch all results
# tables = cursor.fetchall()
# # find items on teble lotto_api_lottop1
# cursor.execute("SELECT * FROM lotto_api_lottop1")
# # Fetch all results
# items = cursor.fetchall()
# for item in items:
#     print('space')
#     print(item)

# # Print the table names
# for table in tables:
#     print(table[0])

# Close the connection
conn.close()
