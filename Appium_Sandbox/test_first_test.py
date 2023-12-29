import time
from appium.options.common import AppiumOptions
from appium import webdriver
from typing import Dict ,Any

from appium.webdriver.common.appiumby import AppiumBy

desired_cap :Dict[str,Any] = {
    "deviceName": "macemulator",
    "platformName": "Android",
    "app": "C:\\Users\\hp\\Downloads\\com.afwsamples.testdpc_9.0.1-9001_minAPI21(nodpi)_apkmirror.com.apk",
    "appPackage": "com.afwsamples.testdpc",
    "appActivity": "com.afwsamples.testdpc.SetupManagementLaunchActivity"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", options=AppiumOptions().load_capabilities(desired_cap))

driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='Next']").click()
time.sleep(10)
driver.find_element(AppiumBy.ID,"com.android.managedprovisioning:id/next_button").click()
time.sleep(10)
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='Next']").click()
time.sleep(10)
driver.find_element(AppiumBy.XPATH,"//android.widget.Button[@text='Finish']").click()


