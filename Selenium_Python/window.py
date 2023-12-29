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

driver.find_element(By.ID,"openwindow").click()
time.sleep(3)
listwindows = driver.window_handles
print(listwindows)
driver.switch_to.window(listwindows[0])
print(driver.title)
time.sleep(5)
driver.close()
time.sleep(3)
driver.switch_to.window(listwindows[1])
print(driver.title)
time.sleep(3)
