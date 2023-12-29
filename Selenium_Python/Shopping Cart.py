import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj=Service()
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.XPATH,"//input[@class='search-keyword']").send_keys("CA")
time.sleep(1)

driver.find_element(By.CLASS_NAME,"search-button").click()



# Country = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item']")
# # for i in Country:
# #     if i.text =="India
# ":
# #         i.click()
# #         break
# # time.sleep(3)
#
additems = driver.find_element(By.XPATH,"//div[@class='products']")
#print("The number of Items with ca are", len(listOfItems))
#print(len(additems))

driver.find_element(By.XPATH,"//h4[text()='Cauliflower - 1 Kg']/following::button[1]").click()
driver.find_element(By.XPATH,"//h4[text()='Carrot - 1 Kg']/following::button[1]").click()
driver.find_element(By.XPATH,"//h4[text()='Capsicum']/following::button[1]").click()
driver.find_element(By.XPATH,"//h4[text()='Cashews - 1 Kg']/following::button[1]").click()
driver.find_element(By.XPATH,"//a[@class='cart-icon']").click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(2)


time.sleep(2)

# for item in additems:
# addbutton = item.find_element(By.CLASS_NAME, "increment").click()
# cart = item.find_element(By.XPATH, ".//button[contains(text(),'ADD TO CART')]")
# cart.click()
# addedcarttext =
# assert addedcarttext == "addedcart.get_attribute('class')print(addedcarttext)"

cauli = driver.find_element(By.XPATH,"//tr[1]//td[5]/p[@class='amount']").get_attribute("text")
carrot = driver.find_element(By.XPATH,"//tr[2]//td[5]/p[@class='amount']").get_attribute("class")
capsi = driver.find_element(By.XPATH,"//tr[3]//td[5]/p[@class='amount']").get_attribute("class")
cashew = driver.find_element(By.XPATH,"//tr[4]//td[5]/p[@class='amount']").get_attribute("class")

print(cauli)
time.sleep(2)


