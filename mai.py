"""
Main entry point to number collector scripts
"""
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Set up Firefox options
options = Options()
options.headless = True  # Run in headless mode

# Initialize the WebDriver
driver = webdriver.Firefox(options=options)

# Open a webpage
driver.get("https://www.google.com")

# Print the title of the page
print(driver.title)

# Close the browser
driver.quit()


