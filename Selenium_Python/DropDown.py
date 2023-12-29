import time
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj=Service()
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

# #select class dropdown

# time.sleep(3)
# dd = Select(driver.find_element(By.ID,"dropdown-class-example"))
# dd.select_by_visible_text("Option1")
# time.sleep(3)
# dd.select_by_index(1)
# time.sleep(3)
# dd.select_by_value("option3")






#
# #dynamic dropdown
#
# countryvalue = "India"
# driver.find_element(By.ID,"autocomplete").send_keys("ind")
# time.sleep(3)
# Country = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item']")
# for i in Country:
#     if i.text =="India":
#         i.click()
#         break
# time.sleep(3)
# value = driver.find_element(By.ID,"autocomplete").is_displayed()
# time.sleep(3)
#
# #CAPTURE THE TEXT THAT IS DISPLAYING
# print(driver.find_element(By.ID,"autocomplete").get_attribute("value"))
# time.sleep(3)
#
# expooutcome = driver.find_element(By.ID,"autocomplete").get_attribute("value")
# time.sleep(3)
# assert expooutcome == countryvalue






#Checkbox
checkbox = driver.find_element(By.ID,"checkBoxOption1")
checkbox.click()
checkbox.is_selected()
time.sleep(2)



checkbox2 = driver.find_element(By.ID,"//label//*[@type='checkbox']")
print(len(checkbox2))
time.sleep(2)


#Radio button
