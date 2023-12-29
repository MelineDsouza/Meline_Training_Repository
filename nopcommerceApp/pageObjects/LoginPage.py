from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_Login_xpath = "//button[@class='button-1 login-button']"
    button_Logout_linktext = "Logout"


    def __init__(self,driver):
        self.driver = driver

    def enter_UserName(self,username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def enter_Password(self,password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_Login(self):
        self.driver.find_element(By.XPATH, self.button_Login_xpath).click()

    def click_Logout(self):
        self.driver.find_element(By.LINK_TEXT, self.button_Logout_linktext).click()

