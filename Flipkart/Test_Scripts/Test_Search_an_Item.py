import time
from selenium.webdriver.chrome import webdriver
from selenium.webdriver import Keys, ActionChains
from POM_classes.Home_Page import Home
from Test_Scripts.conftest import setup
# class Test_Login_1(Login):
#     # name="Admin"
#     # pwd="admin123"

def test_filter_i_phones(setup):
    obj = Home(setup)
    obj.Close_Login_popup()
    obj.SearchButton(search="iphone")
    obj.HitEnter()
    obj.selectApplefilter_button()
    obj.select_Rating_filter_button()
    obj.select_Battery_filter_button()
    obj.display_filtered_items()






