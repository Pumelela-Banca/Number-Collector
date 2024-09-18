"""
Module that selects dates and sorts the month
"""
import time
from selenium.webdriver.common.by import By
from datetime import datetime, timedelta


def find_date(date_string, day, driver):
    """
    Finds a date in the date picker and selects it
    date format: 'September 2024'
    """
    # Open the date picker
    """
    date_obj.strftime("%B")
    """
    time.sleep(2)
    date_picker = driver.find_element(By.XPATH, "//input[@id='fromDate']")
    date_picker.click()
    new_date_string = date_string.split(" ")
    date_obj = datetime(int(new_date_string[0]), int(new_date_string[1]), day=day)
    new_date = date_obj + timedelta(days=1)
    date_string = f"{new_date.strftime('%B')} {new_date.year}"
    print(date_string)
    day = new_date.day

    # Navigate to the desired month and year
    while True:
        month_year = driver.find_element(By.XPATH, '//th[@class="datepicker-switch"]').text
        if month_year == date_string:
            driver.find_element(By.XPATH, f'//td[text()="{day}" and @class="day"]').click()
            break
        prev_button = driver.find_element(By.XPATH, '//th[@class="prev"]')
        prev_button.click()
