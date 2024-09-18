"""
Main entry point to number collector scripts
"""
import datetime
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

db = sqlite3.connect('db.sqlite3')


# Open a webpage
for url in draws_urls:
    driver.get(url)
    # Check date date of the last draw
    
    # Select the start draw date
    if url == "https://www.nationallottery.co.za/lotto-history":
        date_last = find_last_date("LottoP1")
        find_date(f"{date_last.year} {date_last.month}", date_last.day, driver)
        db_name = "lotto_api_lottop1"
        name = "Lotto"
        spfc_name = "LottoP1"
    elif url == "https://www.nationallottery.co.za/powerball-history":
        date_last = find_last_date("Powerball")
        find_date(f"{date_last.year} {date_last.month}", date_last.day, driver)
        db_name = "lotto_api_powerball"
        name = "Powerball"
        spfc_name = "Powerball"
    elif url == "https://www.nationallottery.co.za/powerball-plus-history":
        date_last =  find_last_date("PowerballP1")
        find_date(f"{date_last.year} {date_last.month}", date_last.day, driver)
        db_name = "lotto_api_powerballp1"
        name = "Powerball"
        spfc_name = "PowerballP1"
    elif url == "https://www.nationallottery.co.za/daily-lotto-history":
        date_last = find_last_date("DailyLotto")
        find_date(f"{date_last.year} {date_last.month}", date_last.day, driver)
        db_name = "lotto_api_daily"
        name = "Daily"
        spfc_name = "DailyLotto"
    elif url == "https://www.nationallottery.co.za/lotto-plus-1-history":
        date_last = find_last_date("LottoP2")
        find_date(f"{date_last.year} {date_last.month}", date_last.day, driver)
        db_name = "lotto_api_lottop2"
        name = "Lotto"
        spfc_name = "LottoP2"
    elif url == "https://www.nationallottery.co.za/lotto-plus-2-history":
        date_last = find_last_date("LottoP3")
        find_date(f"{date_last.year} {date_last.month}", date_last.day, driver)
        db_name = "lotto_api_lottop3"
        name = "Lotto"
        spfc_name = "LottoP3"

    driver.implicitly_wait(3)
    pick_today_date(driver) # Pick todays date on the second calender
    driver.find_element(By.XPATH, '//div[@class="btnBox" and text() ="Search"]').click()
    
    get_numbers_from_web = ManageDrawsNavigation(driver,db=db, db_name=db_name)
    get_numbers_from_web.click_draws(name)
    save_last_date(spfc_name, get_numbers_from_web.last_date)
    print(spfc_name, "Done")
      


# close db
db.close()
# Close the browser
driver.quit()
print("done")
