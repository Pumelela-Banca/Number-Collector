"""
saves the data to the database
"""

import sqlite3
from datetime import datetime

# Create a connection to the database
conn = sqlite3.connect('db.sqlite3')

# Create a cursor object
curs = conn.cursor()



curs.execute('''
INSERT INTO LottoP1 (
    draw_date,
    number_1, number_2, number_3, number_4, number_5, number_6, bonus_number,
    div_winners_1, div_winners_2, div_winners_3, div_winners_4, div_winners_5,
    div_winners_6, div_winners_7, div_winners_8, div_prise_1, div_prise_2,
    div_prise_3, div_prise_4, div_prise_5, div_prise_6, div_prise_7, div_prise_8
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
''', (date ,1, 2, 3, 4, 5, 6, 7, 10, 20, 30, 40, 50, 60, 70, 80, 100.0, 200.0, 300.0, 400.0, 500.0, 600.0, 700.0, 800.0))

# Commit the transaction
conn.commit()
