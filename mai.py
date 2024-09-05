"""
Main entry point to number collector scripts
"""
from datetime import datetime
import sqlite3
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from pick_date import find_date
from pick_today_date import pick_today_date
from click_draws import ManageDrawsNavigation


# Set up Firefox options
options = Options()
options.add_argument("-headless")

# Initialize the WebDriver
driver = webdriver.Firefox(options=options)

draws_urls = ["https://www.nationallottery.co.za/lotto-history",
              "https://www.nationallottery.co.za/powerball-history",
              "https://www.nationallottery.co.za/powerball-plus-history",
              "https://www.nationallottery.co.za/daily-lotto-history",
              "https://www.nationallottery.co.za/lotto-plus-1-history",
              "https://www.nationallottery.co.za/lotto-plus-2-history",
              "https://www.nationallottery.co.za/daily-lotto-history",
              "https://www.nationallottery.co.za/daily-lotto-history"]


# Open a webpage
for url in draws_urls:
    driver.get(url)
    # Check date date of the last draw
    
    # Select the start draw date
    if url == "https://www.nationallottery.co.za/lotto-history":
        find_date("March 2000", 1, driver)
        db_name = "LottoP1"
        name = "Lotto"
    elif url == "https://www.nationallottery.co.za/powerball-history":
        find_date("October 2009", 1, driver)
        db_name = "Powerball"
        name = "Powerball"
    elif url == "https://www.nationallottery.co.za/powerball-plus-history":
        find_date("November 2015", 1, driver)
        db_name = "PowerballP1"
        name = "Powerball"
    elif url == "https://www.nationallottery.co.za/daily-lotto-history":
        find_date("March 2019", 1, driver)
        db_name = "DailyLotto"
        name = "Daily"
    elif url == "https://www.nationallottery.co.za/lotto-plus-1-history":
        find_date("November 2003", 1, driver)
        db_name = "LottoP2"
        name = "Lotto"
    elif url == "https://www.nationallottery.co.za/lotto-plus-2-history":
        find_date("August 2017", 1, driver)
        db_name = "LottoP3"
        name = "Lotto"

    pick_today_date(driver) # Pick todays date on the second calender
    driver.find_element_by_xpath('//div[@class="btnBox" and text() ="Search"]').click()
    ManageDrawsNavigation(driver).click_draws(name)
      



# Print the title of the page

# Close the browser
driver.quit()


