from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('http://yourwebsite.com/datepicker')

# Open the date picker
date_picker = driver.find_element(By.ID, 'datePickerId')
date_picker.click()

# Navigate to the desired month and year
while True:
    month_year = driver.find_element(By.CLASS_NAME, 'monthYearSelector').text
    if month_year == 'September 2024':
        break
    next_button = driver.find_element(By.CLASS_NAME, 'nextButton')
    next_button.click()

# Select the day
day = driver.find_element(By.XPATH, "//td[text()='2']")
day.click()

def find_date(date_string, day):
    """
    Finds a date in the date picker and selects it
    """
    # Open the date picker
    date_picker = driver.find_element(By.XPATH, "//input[@id='fromDate']")
    date_picker.click()

    # Navigate to the desired month and year
    while True:
        month_year = driver.find_element(By.CLASS_NAME, 'monthYearSelector').text
        if month_year == date_string:
            break
        next_button = driver.find_element(By.CLASS_NAME, 'next')


