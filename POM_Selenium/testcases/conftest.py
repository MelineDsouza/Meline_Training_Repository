import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import Service

@pytest.fixture
def setup():
    service_obj=Service()
    driver = webdriver.Chrome(service=service_obj)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.close()