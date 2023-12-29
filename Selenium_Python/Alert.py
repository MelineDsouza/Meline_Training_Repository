
import time
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

driver.find_element(By.ID,"alertbtn").click()
time.sleep(2)
alt = driver.switch_to.alert
time.sleep(2)
#alt.accept()
# #alt.dismiss()
#print(alt.text)
time.sleep(2)

#alt.send_keys("sunil")

driver.implicitly_wait(15)
alrttext = alt.text
assert "Hello , share this practice page and share your knowledge" in alrttext
#alt.send_keys("sunil")

wait = WebDriverWait(driver,15)
wait.until(expected_conditions.visibility_of_element_located(By.ID,"wertyudf"))