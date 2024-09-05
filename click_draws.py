"""
Clicks on draws urls
"""

class ManageDrawsNavigation:
    """
    Navigates the draws urls
    """
    def __init__(self, driver):
        self.driver = driver
        self.item = 0
        self.last_date = None

    def click_draws(self, draw_type):
        """
        Clicks on draws urls
        """
        draws = self.driver.find_elements_by_xpath(
            '//div[@class="dataVal dataVal1"]//a[@class="blueLink ank"]')
        self.item = 0
        for draw in draws:
            self.item += 1
            draw.click()
            if len(draws) != 50 and self.item == len(draws):
                # save the last date to json file
                return
            if self.item == 10:
                self.click_next_page()
            
            if draw_type == "Lotto":
                attributes = self.get_attributes_lotto()
            if draw_type == "Powerball":
                attributes = self.get_attributes_powerball()
            else:
                attributes = self.get_attributes_daily()
            # Save the attributes to the database
            # to do
        self.click_draws()

    def amount_of_available_draws(self):
        """
        Returns the amount of available draws
        """
        return len(self.driver.find_elements_by_xpath(
            '//div[@class="dataVal dataVal1"]//a[@class="blueLink ank"]'))

    def click_next_page(self):
        """
        Clicks on the next page
        """
        if self.item == self.amount_of_available_draws():
            self.driver.driver.implicity_wait(2)
            self.item = 0

        self.driver.find_element_by_xpath(
            '//a[@class="next"]//i[@class="fa fa-angle-right"]').click()

    def click_previous_page(self):
        """
        Clicks back to  list of draws
        """
        self.driver.find_element_by_xpath(
            '//span[@id="back"]').click()
        
    def get_attributes_lotto(self):
        """
        Get the attributes of the draw
        """
        # Get the draw date
        draw_date = self.driver.find_element_by_xpath(
            '//span[@id="drawDate"]').text
        if not self.last_date:
            self.last_date = draw_date

        # Get the numbers
        numbers = []
        for number in range(1, 7):
            numbers.append(int(self.driver.find_element_by_xpath(
                f'//li[@id="ball{number}"]//div//span').text))
        numbers.append(self.driver.find_element_by_xpath(
            '//li[@id="bonusball1"]//div//span').text)

        # Get the winners
        winners = []
        for winner in range(1, 9):
            winners.append(int(self.driver.find_element_by_xpath(
                f'//div[@id="div{winner}"]').text))
    
        # Get the prises
        prises = []
        for prise in range(1, 9):
            prises.append(self.convert_prize(self.driver.find_element_by_xpath(
                f'//div[@id="div{prise}Winner"]').text))
        return draw_date, numbers, winners, prises


    def get_attributes_powerball(self):
        """
        Get the attributes of the draw
        """
        # Get the draw date
        draw_date = self.driver.find_element_by_xpath(
            '//span[@id="drawDate"]').text
        if not self.last_date:
            self.last_date = draw_date

        # Get the numbers
        numbers = []
        for number in range(1, 6):
            numbers.append(int(self.driver.find_element_by_xpath(
                f'//li[@id="ball{number}"]//div//span').text))
        numbers.append(int(self.driver.find_element_by_xpath(
            '//li[@id="bonusball1"]//div//span').text))

        # Get the winners
        winners = []
        for winner in range(1, 10):
            winners.append(int(self.driver.find_element_by_xpath(
                f'//div[@id="div{winner}"]').text))

        # Get the prises
        prises = []
        for prise in range(1, 10):
            prises.append(self.convert_prize(self.driver.find_element_by_xpath(
                f'//div[@id="div{prise}Winner"]').text))
        return draw_date, numbers, winners, prises
        

    def get_attributes_daily(self):
        """
        Get the attributes of the draw
        """
        # Get the draw date
        draw_date = self.driver.find_element_by_xpath(
            '//span[@id="drawDate"]').text
        if not self.last_date:
            self.last_date = draw_date

        # Get the numbers
        numbers = []
        for number in range(1, 6):
            numbers.append(int(self.driver.find_element_by_xpath(
                f'//li[@id="ball{number}"]//div//span').text))

        # Get the winners
        winners = []
        for winner in range(1, 5):
            winners.append(int(self.driver.find_element_by_xpath(
                f'//div[@id="div{winner}"]').text))

        # Get the prises
        prises = []
        for prise in range(1, 5):
            prises.append(self.convert_prize(self.driver.find_element_by_xpath(
                f'//div[@id="div{prise}Winner"]').text))
        return draw_date, numbers, winners, prises

    def convert_prize(self, prize):
        """
        Converts the prize to float
        """
        return float(prize.replace("R", "").replace(",", ""))
