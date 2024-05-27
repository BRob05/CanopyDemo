import pytest
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from pages.swaglogin import SwagLogin


@pytest.fixture()
def driver():
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()


def test_SuccessLogin(driver):
    login_page = SwagLogin(driver)
    login_page.openSwagLabs("https://www.saucedemo.com/")
    time.sleep(1)
    login_page.enterUsername("standard_user")
    login_page.enterPassword("secret_sauce")
    login_page.clickLoginButton()
    time.sleep(3)