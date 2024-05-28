import sys
sys.path.append(".")
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    login_page.enterUsername("standard_user")
    login_page.enterPassword("secret_sauce")
    login_page.clickLoginButton()
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='app_logo']")))
    assert driver.find_element(By.XPATH,"//div[@class='app_logo']").is_displayed()

def test_NoUsername(driver):
    login_page = SwagLogin(driver)
    
    login_page.openSwagLabs("https://www.saucedemo.com/")
    login_page.enterUsername("")
    login_page.enterPassword("secret_sauce")
    login_page.clickLoginButton()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']")))
    element_text = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    expected_text = "Epic sadface: Username is required"

    assert element_text == expected_text

def test_NoPassword(driver):
    login_page = SwagLogin(driver)
    
    login_page.openSwagLabs("https://www.saucedemo.com/")
    login_page.enterUsername("standard_user")
    login_page.enterPassword("")
    login_page.clickLoginButton()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']")))
    element_text = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    expected_text = "Epic sadface: Password is required"

    assert element_text == expected_text

def test_LockedOutUser(driver):
    login_page = SwagLogin(driver)
    
    login_page.openSwagLabs("https://www.saucedemo.com/")
    login_page.enterUsername("locked_out_user")
    login_page.enterPassword("secret_sauce")
    login_page.clickLoginButton()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']")))
    element_text = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    expected_text = "Epic sadface: Sorry, this user has been locked out."

    assert element_text == expected_text

def test_InvalidCredentials(driver):
    login_page = SwagLogin(driver)
    
    login_page.openSwagLabs("https://www.saucedemo.com/")
    login_page.enterUsername("sdfgfgr")
    login_page.enterPassword("rg5345")
    login_page.clickLoginButton()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h3[@data-test='error']")))
    element_text = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    expected_text = "Epic sadface: Username and password do not match any user in this service"

    assert element_text == expected_text