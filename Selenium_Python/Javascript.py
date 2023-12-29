from selenium import webdriver
import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj=Service()
driver=webdriver.Chrome(service=service_obj)
# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.maximize_window()

# btn = driver.find_element(By.XPATH("")).click()
# driver.execute_script("arguments[0].click();"btn)

#
# btn = driver.find_element(By.NAME, "username[0]")
# driver.execute_script("arguments[0].click()", btn)

# btn = driver.find_element(By.NAME, "username[0]")
# driver.execute_script("arguments[0].value('Admin')", btn)
#








# driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# btn = driver.find_element(By.ID, "autocomplete")
# driver.execute_script("arguments[0].value='meline';", btn)
#
# time.sleep(2)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(10)

time.sleep(2)
driver.find_element(By.NAME,"username").click()

btn = driver.find_element(By.NAME, "username")
driver.execute_script("arguments[0].value='Admin';", btn)
time.sleep(2)

driver.find_element(By.XPATH,"//img[@alt='company-branding']").click()
time.sleep(5)

btn2 = driver.find_element(By.NAME, "password")
driver.execute_script("arguments[0].value='admin123';", btn2)
time.sleep(3)

driver.find_element(By.XPATH,"//img[@alt='company-branding']").click()
time.sleep(5)

driver.find_element(By.XPATH,"//button[text()=' Login ']").click()
time.sleep(5)

# driver.execute_script("window.scrollTo(0,500);")
# time.sleep(2)
# -1,0





