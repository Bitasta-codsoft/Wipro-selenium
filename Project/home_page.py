from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    # Search box
    search_box = (By.NAME, "search")

    # Search button
    search_button = (By.CSS_SELECTOR, "button.btn.btn-default.btn-lg")

    def search_product(self, product_name):
        self.driver.find_element(*self.search_box).clear()
        self.driver.find_element(*self.search_box).send_keys(product_name)
        self.driver.find_element(*self.search_button).click()