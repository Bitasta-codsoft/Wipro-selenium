from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    # Cart page elements
    quantity_field = (By.CSS_SELECTOR, "input[name^='quantity']")
    update_button = (By.CSS_SELECTOR, "button[data-original-title='Update']")

    def update_quantity(self, quantity):
        quantity_input = self.driver.find_element(*self.quantity_field)

        quantity_input.clear()
        quantity_input.send_keys(str(quantity))

        self.driver.find_element(*self.update_button).click()

    def get_quantity(self):
        # Retry if the cart refreshes and replaces the quantity element
        def read_quantity(driver):
            try:
                quantity_input = driver.find_element(*self.quantity_field)
                return quantity_input.get_attribute("value")
            except StaleElementReferenceException:
                return False

        return WebDriverWait(self.driver, 10).until(read_quantity)