import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

service_obj=Service()
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()


Action = ActionChains(driver)
Action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
time.sleep(2)
Action.key_down(Keys.ARROW_DOWN).perform()
time.sleep(2)
Action.key_down(Keys.ENTER).perform()
time.sleep(2)


Action.context_click(driver.find_element(By.ID,"mousehover")).perform()
# time.sleep(2)
#Action.key_down(Keys.CONTROL).key_up(Keys.TAB).perform()
Action.key_up(Keys.CONTROL+Keys.TAB).perform()
Action.release().perform()
time.sleep(2)
#upload

# Action.context_click().perform()
# Action.double_click().perform()
# Action.drag_and_drop().perform()
# Action.key_up().perform()
# Action.key_down()
#