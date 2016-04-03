from selenium import webdriver
from RamblerModels.application import Application
import pytest

@pytest.fixture(scope="module")
def ramblerapp(request, browser_type, base_url):
    if browser_type == "firefox":
        driver = webdriver.Firefox()
    #driver.implicitly_wait(60)
    request.addfinalizer(driver.quit)
    return Application(driver, base_url)
