from pytest import fixture
from appium import webdriver
from typing import Dict,Any
from appium.options.common import AppiumOptions

@fixture(scope="class")  #function instead of class if it is connected
def setup_driver():
    desired_cap : Dict[str,Any] = {
    "deviceName": "macemulator",
    "platformName": "Android",
    "app": r"C:\\Users\\hp\\Downloads\\com.afwsamples.testdpc_9.0.1-9001_minAPI21(nodpi)_apkmirror.com.apk",
    "appPackage": "com.afwsamples.testdpc",
    "appActivity": "com.afwsamples.testdpc.SetupManagementLaunchActivity"}
    driver = webdriver.Remote(r"http://localhost:4723/wd/hub", options=AppiumOptions().load_capabilities(desired_cap))
    yield driver
