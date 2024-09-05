"""
Last date for each draw will  be  stored in json files in the format of:
{LottoP1: '2023-09-04', Powerball: '2023-09-04', 
PowerballP1: '2023-09-04', DailyLotto: '2023-09-04', 
LottoP2: '2023-09-04', LottoP3: '2023-09-04'}
"""
import json
from datetime import datetime


def save_last_date(draw_type, date):
    """
    Save the last date of the draw
    """
    with open('last_draw_dates.json', 'r') as file:
        data = json.load(file)
        data[draw_type] = date
    with open('last_draw_dates.json', 'w') as file:
        json.dump(data, file)


def find_last_date(draw_type):
    """
    Find the last date of the draw
    """
    with open('last_draw_dates.json', 'r') as file:
        data = json.load(file)
        return datetime.strptime(data[draw_type], '%Y-%m-%d')
