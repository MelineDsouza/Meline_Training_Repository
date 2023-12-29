import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
# from Flipkart.generic_functions.selenium_functions import selenium_wrapper
from generic_functions.selenium_functions import selenium_wrapper12

class Home(selenium_wrapper12):
    close_Popup ="//*[@class='_30XB9F']"
    searchButton="Pke_EE"
    brand_filter ="//div[text()='APPLE']"

    rating ="//div[text()='4★ & above']"
    battery_expand = "// div[text() = 'Battery Capacity']"
    battery_Range ="// div[text() = '2000 - 2999 mAh']"
    display_filter="//div[@class='_1xc7yr']"

    homeFurniture="// span[text() = 'Home & Furniture']"
    # Logout_link = "Logout"

    # def __init__(self,driver):
    #     self.driver=driver
    #

    def Close_Login_popup(self):
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.close_Popup).click()


    def SearchButton(self,search):
        time.sleep(5)
        self.driver.find_element(By.CLASS_NAME,self.searchButton).send_keys(search)

    def HitEnter(self):
        Action = ActionChains(self.driver)
        Action.key_down(Keys.ENTER).perform()
        time.sleep(5)

    def selectApplefilter_button(self):
        # self.clicking_on_element(self.brand_filter).click()  # click_element(self,(By.CLASS_NAME,"ico-register"))
        self.driver.find_element(By.XPATH,self.brand_filter).click()
        time.sleep(5)

    def select_Rating_filter_button(self):
        self.driver.find_element(By.XPATH, self.rating).click()
        time.sleep(5)

    def select_Battery_filter_button(self):
        self.driver.find_element(By.XPATH, self.battery_expand).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.battery_Range).click()
        time.sleep(5)

    def display_filtered_items(self):
        print(self.driver.find_element(By.XPATH, self.display_filter).text)
        time.sleep(5)



def display_filtered_items(self):
    print(self.driver.find_element(By.XPATH, self.homeFurniture).click)
    time.sleep(5)

