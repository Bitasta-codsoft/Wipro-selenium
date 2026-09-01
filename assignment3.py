from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# CSS selector using ID
name_field = driver.find_element(
    By.CSS_SELECTOR, "#name"
)

name_field.send_keys("Bitasta")


# CSS selector using attribute
radio2 = driver.find_element(
    By.CSS_SELECTOR,
    "input[value='radio2']"
)

radio2.click()


# CSS selector using type
checkboxes = driver.find_elements(
    By.CSS_SELECTOR,
    "input[type='checkbox']"
)

print(
    "\nCheckboxes found using CSS:",
    len(checkboxes)
)


# CSS wildcard example
# Finds elements whose ID starts with "radio"
radio_elements = driver.find_elements(
    By.CSS_SELECTOR,
    "input[value^='radio']"
)

print(
    "Elements whose value starts with radio:",
    len(radio_elements)
)
driver.quit()