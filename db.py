"""
saves the data to the database
"""
import sqlite3
from datetime import datetime


def insert_into_tables(table_name, data_tuple, cursor, attributes):
    """
    Runs insetion into table
    """
    data = (attributes[0], *attributes[1], *attributes[2], *attributes[3])
    if table_name in ['LottoP1', 'LottoP3', 'LottoP2']:
        
        cursor.eexecute(f'''
                        INSERT INTO {table_name} (
                            draw_date,
                            number_1, number_2, number_3, number_4, number_5, number_6, bonus_number,
                            div_winners_1, div_winners_2, div_winners_3, div_winners_4, div_winners_5,
                            div_winners_6, div_winners_7, div_winners_8, div_prise_1, div_prise_2,
                            div_prise_3, div_prise_4, div_prise_5, div_prise_6, div_prise_7, div_prise_8
                        ) VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', data )
    elif table_name in ['Powerball', 'PowerballP1']:
        cursor.eexecute(f'''
                        INSERT INTO {table_name} (
                            draw_date,
                            number_1, number_2, number_3, number_4, number_5, bonus_number,
                            div_winners_1, div_winners_2, div_winners_3, div_winners_4, div_winners_5,
                            div_winners_6, div_winners_7, div_winners_8, div_winners_9, div_prise_1, div_prise_2,
                            div_prise_3, div_prise_4, div_prise_5, div_prise_6, div_prise_7, div_prise_8, div_prise_9
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', data )
    else:
        cursor.eexecute(f'''
                        INSERT INTO {table_name} (
                            draw_date,
                            number_1, number_2, number_3, number_4, number_5,
                            div_winners_1, div_winners_2, div_winners_3, div_winners_4, div_prise_1, div_prise_2,
                            div_prise_3, div_prise_4) VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', data )
