import time

import pytest
from selenium import webdriver


@pytest.fixture(params=["chrome", "firefox"], scope="class")
def driver_init(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    if request.param == "firefox":
        web_driver = webdriver.Firefox()
    # if request.param == "MicrosoftEdge":
    #     web_driver = webdriver.Edge(executable_path=r'C:\EdgeDriver\MicrosoftWebDriver.exe')
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass


class Test_URL(BasicTest):
    def test_open_url(self):
        self.driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        print(self.driver.title)
        time.sleep(5)