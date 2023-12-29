import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path=".//TestData/LoginData.xlsx"

    logger = LogGen.loggen()


    def test_Login_ddt(self,setup):
        self.logger.info("************* Test_002_DDT_Login ****************")
        self.logger.info("*************Verifying Login test ****************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)

        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of Rows in a Excel:",self.rows)

        list_status=[]   #empty list variable


        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.path,'Sheet1',r,2)
            self.exp = XLUtils.readData(self.path,'Sheet1',r,3)


            self.lp.enter_UserName(self.user)
            self.lp.enter_Password(self.password)
            self.lp.click_Login()
            time.sleep(5)


            actual_title_homepage = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"

            if actual_title_homepage==expected_title:
                if self.exp == "Pass" :
                    self.logger.info("************* test is passed ****************")
                    self.lp.click_Logout()
                    list_status.append("Pass")
                elif self.exp == "Fail" :
                    self.logger.info("************* failed ****************")
                    self.lp.click_Logout()
                    list_status.append("Fail")

            elif actual_title_homepage !=  expected_title:
                if self.exp == "Pass" :
                    self.logger.info("************* failed ****************")
                    self.lp.click_Logout()
                    list_status.append("Fail")
                elif self.exp == "Fail" :
                    self.logger.info("************* passed ****************")
                    self.lp.click_Logout()
                    list_status.append("Pass")

        if "Fail" not in list_status :
            self.logger.info("************* login DDT test is passed ****************")
            self.driver.close()
            assert True
        else:
            self.logger.info("************* login DDT test is failed ****************")
            self.driver.close()
            assert False

        self.logger.info("************* End of Login DDT Test ****************")
        self.logger.info("************* Competed TC_Login_DDT_002 ****************")

