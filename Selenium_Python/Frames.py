from selenium import webdriver
import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
driver.get("https://demoqa.com/frames")
driver.maximize_window()

driver.switch_to.frame("frame2")
text = driver.find_element(By.ID,"sampleHeading").text
print(text)
driver.switch_to.default_content()
print(driver.title)

time.sleep(3)
driver.save_screenshot('mac.png')
time.sleep(3)
driver.get_screenshot_as_png()
time.sleep(3)
driver.get_screenshot_as_file('mel.png')
