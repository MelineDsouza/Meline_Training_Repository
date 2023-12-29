from selenium import webdriver
import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()


Action = ActionChains(driver)
Action.move_to_element(driver.find_element(By.ID,"product")).perform()

time.sleep(2)
table = driver.find_element(By.ID,"product")
allRows = table.find_elements(By.TAG_NAME,"tr")
for row in allRows:
    cells = row.find_elements(By.TAG_NAME,"td")
    for cell in cells:
     pass
    print(driver.find_element(By.TAG_NAME,"th").text)

time.sleep(2)


//*[@id='product'][2]/tbody/tr[2]/td/preceding-sibling::