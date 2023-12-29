import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup():
    print("first")
    yield
    print("last")

@pytest.fixture()
def data():
   return ["mel","mac","dsouz"]


@pytest.fixture(params=["chrome","firefox"])
def data2(browser):
   return browser.params




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
