import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    username="username"
    password="password"
    login_submit_btn="//*[@typ='submit']"
    Logout_dropdown_btn="//*[@class='oxd-userdropdown-name']"
    Logout_link = "Logout"

    def __init__(self,driver):
        self.driver=driver

    def test_Enter_username(self,name):
        time.sleep(10)
        self.driver.find_element(By.NAME,self.username).send_keys(name)

    def test_Enter_password(self,pwd):
        time.sleep(10)
        self.driver.find_element(By.NAME,self.password).send_keys(pwd)
