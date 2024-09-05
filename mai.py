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
from find_last_date import save_last_date, find_last_date


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

# See if the database exists  last date is in last_draw_dates.json



# Open a webpage
for url in draws_urls:
    driver.get(url)
    # Check date date of the last draw
    
    # Select the start draw date
    if url == "https://www.nationallottery.co.za/lotto-history":
        date_last = find_last_date("LottoP1")
        find_date(f"{date_last.year} {date_last.month}", int(date_last.day), driver)
        db_name = "LottoP1"
        name = "Lotto"
    elif url == "https://www.nationallottery.co.za/powerball-history":
        date_last = find_last_date("Powerball")
        find_date(f"{date_last.year} {date_last.month}", int(date_last.day), driver)
        db_name = "Powerball"
        name = "Powerball"
    elif url == "https://www.nationallottery.co.za/powerball-plus-history":
        date_last =  find_last_date("PowerballP1")
        find_date(f"{date_last.year} {date_last.month}", int(date_last.day), driver)
        db_name = "PowerballP1"
        name = "Powerball"
    elif url == "https://www.nationallottery.co.za/daily-lotto-history":
        date_last = find_last_date("DailyLotto")
        find_date(f"{date_last.year} {date_last.month}", int(date_last.day), driver)
        db_name = "DailyLotto"
        name = "Daily"
    elif url == "https://www.nationallottery.co.za/lotto-plus-1-history":
        date_last = find_last_date("LottoP2")
        find_date(f"{date_last.year} {date_last.month}", int(date_last.day), driver)
        db_name = "LottoP2"
        name = "Lotto"
    elif url == "https://www.nationallottery.co.za/lotto-plus-2-history":
        date_last = find_last_date("LottoP3")
        find_date(f"{date_last.year} {date_last.month}", int(date_last.day), driver)
        db_name = "LottoP3"
        name = "Lotto"

    pick_today_date(driver) # Pick todays date on the second calender
    driver.find_element_by_xpath('//div[@class="btnBox" and text() ="Search"]').click()

    get_numbers_from_web = ManageDrawsNavigation(driver)
    get_numbers_from_web.click_draws(name)
    save_last_date(name, get_numbers_from_web.last_date)
      

# Close the browser
driver.quit()


