import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
# from Flipkart.generic_functions.selenium_functions import selenium_wrapper
from generic_functions.selenium_functions import selenium_wrapper12

class Home(selenium_wrapper12):
    clockbutton ="//a[text()='Clocks']"


    def selectfurniture(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.clockbutton).click()


