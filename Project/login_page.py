from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # Login page elements
    email_field = (By.ID, "input-email")
    password_field = (By.ID, "input-password")
    login_button = (By.CSS_SELECTOR, "input[type='submit']")

    def enter_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()