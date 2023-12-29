# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
# #(executable_path  ="C:\\Users\\hp\\Downloads\\chromedriver_win32\\chromedriver.exe)
#
#
# service_obj=Service()
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#
# driver.maximize_window()
# # driver.minimize_window()
# # print(driver.title)
# # print(driver.current_url)
# #driver.close()
# #driver.quit()
#
# # driver.find_element(By.NAME,"username")
# # driver.find_element(By.XPATH,"//input[@name='username']")
# # driver.find_element(By.CSS_SELECTOR,"input[name='username']")
# # driver.find_element(By.CLASS_NAME,"oxd-input oxd-input--active")
# # driver.find_element(By.CSS_SELECTOR,".oxd-input oxd-input--active")
#
# time.sleep(5)
#
# driver.find_element(By.XPATH('//input[@name="username"]')).send_keys("Admin")
#



import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj=Service()
driver = webdriver.Chrome(service=service_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()


time.sleep(5)
driver.find_element(By.NAME,"username").send_keys('Admin')
driver.find_element(By.NAME,"password").send_keys('admin123')
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
time.sleep(5)

#driver.forward()
#driver.back()
#driver.refresh()
time.sleep(5)

driver.find_element(By.LINK_TEXT,"PIM").click()

# #static dropdown
# dd = Select(driver.find_element(By.CSS_SELECTOR,".oxd-select-text"))
# dd.select_by_visible_text("Full-Time Contract")
# dd.select_by_index(1)
time.sleep(5)

#dynamic drop down
driver.find_element(By.XPATH,"//div[@class='oxd-table-filter']/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/child::input").send_keys("ch")

time.sleep(5)
driver.find_element(By.XPATH,"//span[text()='Charlie  Carter']").click()
time.sleep(5)




