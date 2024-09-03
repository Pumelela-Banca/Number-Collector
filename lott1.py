from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.example.com")

# Click a checkbox
checkbox = driver.find_element(By.id("checkbox_id"))
checkbox.click()

# Click a radio button
radio_button = driver.find_element(By.id("radio_button_id"))
radio_button.click()

driver.quit()
