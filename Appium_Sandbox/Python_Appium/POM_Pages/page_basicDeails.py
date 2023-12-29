from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

class Deails:
    nextbutton = (AppiumBy.XPATH,"//android.widget.Button[@text='Next']")

 #locatore


    def __init__(self,driver):
        self.driver = driver


    def clickNextButton(self):
        self.driver.find_element(*self.nextbutton).click()
        sleep(10)

    def clickbutton(self):
        self.driver.find_element(AppiumBy.ID,"com.android.managedprovisioning:id/next_button").click()
        sleep(10)




class Home:
    def __init__(self,driver):
        self.driver = driver

    def click2ndNextElement(self):
        self.driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='Next']").click()
        sleep(10)


