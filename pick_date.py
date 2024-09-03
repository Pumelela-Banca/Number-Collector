"""
Function
"""
from selenium.webdriver.common.by import By


def find_date(date_string, day, driver):
    """
    Finds a date in the date picker and selects it
    date format: 'September 2024'
    """
    # Open the date picker
    date_picker = driver.find_element(By.XPATH, "//input[@id='fromDate']")
    date_picker.click()

    # Navigate to the desired month and year
    while True:
        month_year = driver.find_element(By.XPATH, '//th[@class="datepicker-switch"]').text
        if month_year == date_string:
            driver.find_element(By.XPATH, f'//td[text()="{day}" and @class="day"]').click()
            break
        prev_button = driver.find_element(By.XPATH, '//th[@class="prev"]')
        prev_button.click()
