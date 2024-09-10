"""
Clicks on draws urls
"""
from datetime import datetime
import sqlite3
from db import insert_into_tables
from selenium.webdriver.common.by import By


class ManageDrawsNavigation:
    """
    Navigates the draws urls
    """
    def __init__(self, driver, db, db_name):
        self.conn = db
        self.curs = self.conn.cursor() 
        self.driver = driver
        self.item = 0
        self.last_date = None
        self.db_name = db_name

    def click_draws(self, draw_type):
        """
        Clicks on draws urls
        """
        self.driver.implicitly_wait(2)
        draws = self.driver.find_elements(By.XPATH,
                                         '//div[@class="dataVal dataVal1"]//a[@class="blueLink ank"]')
        self.item = 0
        for draw in draws:
            self.item += 1
            draw.click()
            
            if draw_type == "Lotto":
                attributes = self.get_attributes_lotto()
            elif draw_type == "Powerball":
                attributes = self.get_attributes_powerball()
            else:
                attributes = self.get_attributes_daily()
            insert_into_tables(self.db_name, cursor=self.curs, attributes=attributes)
            if self.item % 10 == 0:
                self.click_next_page()
            if len(draws) != 50 and self.item == len(draws):
                return
        self.driver.implicitly_wait(3)
        self.click_draws(draw_type=draw_type)

    def amount_of_available_draws(self):
        """
        Returns the amount of available draws
        """
        return len(self.driver.find_elements(By.XPATH, 
                                            '//div[@class="dataVal dataVal1"]//a[@class="blueLink ank"]'))

    def click_next_page(self):
        """
        Clicks on the next page
        """
        if self.item == self.amount_of_available_draws():
            self.driver.implicitly_wait(2)
            self.item = 0

        self.driver.find_element(By.XPATH, 
                                 '//a[@class="next"]').click()

    def click_previous_page(self):
        """
        Clicks back to  list of draws
        """
        self.driver.find_element(By.XPATH,
                                 '//span[@id="back"]').click()
        
    def get_attributes_lotto(self):
        """
        Get the attributes of the draw
        """
        # Get the draw date
        draw_date = self.driver.find_element(By.XPATH, 
                                             '//span[@id="drawDateLotto"]').text
        if not self.last_date:
            self.last_date = draw_date

        # Get the numbers
        numbers = []
        
        for number in range(1, 7):
            num = self.driver.find_element(By.XPATH, 
                                                    f'//li[@id="ball{number}"]//div//span').text
            numbers.append(int(num) if num[0] != "0" else int(num[1]))
        num = self.driver.find_element(By.XPATH, 
                                                '//li[@id="bonusball1"]//div//span').text
        numbers.append(int(num) if num[0] != "0" else int(num[1]))

        # Get the winners
        winners = []
        for winner in range(1, 9):
            winners.append(int(self.driver.find_element(By.XPATH, 
                                                        f'//div[@id="div{winner}"]').text))
    
        # Get the prises
        prises = []
        for prise in range(1, 9):
            prises.append(self.convert_prize(self.driver.find_element(By.XPATH, 
                                                                      f'//div[@id="div{prise}Winner"]').text))
        self.driver.find_element(By.XPATH, '//span[@id="back"]').click()
        return datetime.strptime(draw_date, "%Y-%m-%d"), numbers, winners, prises


    def get_attributes_powerball(self):
        """
        Get the attributes of the draw
        """
        # Get the draw date
        draw_date = self.driver.find_element(By.XPATH, 
                                             '//span[@id="drawDate1"]').text
        if not self.last_date:
            self.last_date = draw_date

        # Get the numbers
        numbers = []
        for number in range(1, 6):
            numbers.append(int(self.driver.find_element(By.XPATH, 
                                                        f'//li[@id="ball{number}"]//div//span').text))
        numbers.append(int(self.driver.find_element(By.XPATH, 
                                                    '//li[@id="bonusball1"]//div//span').text))

        # Get the winners
        winners = []
        for winner in range(1, 10):
            winners.append(int(self.driver.find_element(By.XPATH, 
                                                        f'//div[@id="div{winner}"]').text))

        # Get the prises
        prises = []
        for prise in range(1, 10):
            prises.append(self.convert_prize(self.driver.find_element(By.XPATH, 
                                                                      f'//div[@id="div{prise}Winner"]').text))
        self.driver.find_element(By.XPATH, '//span[@id="back"]').click()
        return datetime.strptime(draw_date, "%Y-%m-%d"), numbers, winners, prises
        
    def get_attributes_daily(self):
        """
        Get the attributes of the draw
        """
        # Get the draw date
        draw_date = self.driver.find_element(By.XPATH, 
                                             '//span[@id="drawDate1"]').text
        if not self.last_date:
            self.last_date = draw_date

        # Get the numbers
        numbers = []
        for number in range(1, 6):
            numbers.append(int(self.driver.find_element(By.XPATH, 
                                                        f'//li[@id="ball{number}"]//div//span').text))

        # Get the winners
        winners = []
        for winner in range(1, 5):
            winners.append(int(self.driver.find_element(By.XPATH, 
                                                        f'//div[@id="div{winner}"]').text))

        # Get the prises
        prises = []
        for prise in range(1, 5):
            prises.append(self.convert_prize(self.driver.find_element(By.XPATH, 
                                                                      f'//div[@id="div{prise}Winner"]').text))
        self.driver.find_element(By.XPATH, '//span[@id="back"]').click()
        return datetime.strptime(draw_date, "%Y-%m-%d"), numbers, winners, prises

    def convert_prize(self, prize):
        """
        Converts the prize to float
        """
        return float(prize.replace("R", "").replace(",", ""))
