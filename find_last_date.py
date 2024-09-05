"""
Last date for each draw will  be  stored in json files in the format of:
{LottoP1: '2023-09-04', Powerball: '2023-09-04', 
PowerballP1: '2023-09-04', DailyLotto: '2023-09-04', 
LottoP2: '2023-09-04', LottoP3: '2023-09-04'}
"""
import json


def save_last_date(draw, date):
    """
    Save the last date of the draw
    """
    with open('last_draw_dates.json', 'r') as file:
        data = json.load(file)
        data[draw] = date
    with open('last_draw_dates.json', 'w') as file:
        json.dump(data, file)
