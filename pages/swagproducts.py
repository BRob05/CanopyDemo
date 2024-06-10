from selenium.webdriver.common.by import By


class SwagProducts:
    def __init__(self, driver):
        self.driver = driver
        self.add_to_cart_button = (By.CLASS_NAME, "btn_primary")
        self.hamburger_button = (By.ID, "react-burger-menu-btn")
        self.remove_button = (By.CLASS_NAME, "btn_secondary")
    
    def addToCart(self):
        self.driver.find_element(*self.add_to_cart_button).click()
    
    def removeFromCart(self):
        self.driver.find_element(*self.remove_button).click()