"""
Picks todays date on second calender
"""
from selenium.webdriver.common.by import By


def pick_today_date(driver):
    """
    Picks todays date on second calender
    """
    # Open the date picker
    date_picker = driver.find_element(By.XPATH, "//input[@id='toDate']")
    date_picker.click()

    # Click on todays date
    driver.find_element(By.XPATH, '//td[text()="Today"]').click()
