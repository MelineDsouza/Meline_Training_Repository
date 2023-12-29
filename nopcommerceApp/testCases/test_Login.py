import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsermail()
    password = ReadConfig.getpassword()

    logger = LogGen.loggen()

    def test_homePage_Tittle(self,setup):
        self.logger.info(" *************Test_001 Login mac ****************")
        self.logger.info(" ************* Verifying Home Page Title ****************")

        self.driver = setup
        self.driver.get(self.baseURL)
        time.sleep(10)

        actualTitle = self.driver.title
        if actualTitle == "Your store. Login" :
            assert True
            self.driver.close()
            self.logger.info("*************Home Page Title test is passed ****************")

        else :
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePage_Tittle.png")
            self.driver.close()
            self.logger.error("*************Home Page Title test is failed ****************")
            assert False


    def test_Login(self,setup):
        self.logger.info("*************Verifying Login test ****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.enter_UserName(self.username)
        self.lp.enter_Password(self.password)
        self.lp.click_Login()

        actual_title_homepage = self.driver.title
        if actual_title_homepage == "Dashboard / nopCommerce administration" :
            assert True
            self.logger.info("*************Login test is passed ****************")
            self.driver.close()
        else :
            self.driver.save_screenshot(".\\Screenshots\\"+"test_Login.png")
            self.logger.info("*************Login test is failed ****************")
            self.driver.close()
            assert False


