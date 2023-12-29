import time
from appium.options.common import AppiumOptions
from appium import webdriver
from typing import Dict ,Any
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction

desired_cap :Dict[str,Any] = {
  "deviceName": "macemulator",
  "platformName": "Android",
  "appPackage": "com.myntra.android",
  "appActivity": "com.myntra.android.activities.react.ReactActivity"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", options=AppiumOptions().load_capabilities(desired_cap))


time.sleep(20)
# element = driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='Finish']").click()
tourch = TouchAction(driver)
tourch.press(x=524, y=1775).move_to(x=513, y=804).release().perform()

for i in range(3):
    tourch = TouchAction(driver)
    time.sleep(10)
    tourch.press(x=524, y=1775).move_to(x=513, y=804).release().perform()

time.sleep(10)

ts = time.strftime("%Y_%m_%d_%H%M%S")
activityname = driver.current_activity
filename = activityname + ts
time.sleep(10)

driver.save_screenshot("/Users/hp/PycharmProjects/dpc_appium_python_proj/Screenshots/"+filename+".png")


