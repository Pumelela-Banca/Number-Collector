"""
Main entry point to number collector scripts
"""
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

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
    # Print the title of the page
    print(driver.title)


# Print the title of the page

# Close the browser
driver.quit()





# div winners //div[@id="div3Winner"] amount
# number of winners //div[@id="div5"]
# get numbers //li[@id='ball23']//div[@class='shape']/span  .text