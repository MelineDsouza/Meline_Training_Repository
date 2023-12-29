from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == 'chrome' :
        driver = webdriver.Chrome()
        print("Launching Chrome browser")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser")
    else:
        driver = webdriver.Ie()
        print("Launching Internet Explorer browser")
    return driver


# gets the value to CLI
def  pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):   #thid will return browser value to setup method
    driver = webdriver.Chrome()
    return request.config.getoption("--browser")


############### Pytest HTML Report #############
#It is a hook for ading enviorment info to HTML report


def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Macline'

#It is a hook for delete or modify Enviorment info to html report
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)


