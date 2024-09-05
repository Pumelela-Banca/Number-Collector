import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('db.sqlite3')
curs = conn.cursor()

# Select the last row from the table
curs.execute('SELECT draw_date FROM LottoP1 ORDER BY id DESC LIMIT 1')

# Fetch the result
last_row = curs.fetchone()
date = last_row[0]

# Close the connection
conn.close()

# Print the last row
print(last_row)
