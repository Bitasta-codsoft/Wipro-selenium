from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# Find input elements inside the radio button section
radio_section_inputs = driver.find_elements(
    By.CSS_SELECTOR,
    "div.left-align input"
)
print(
    "\nInputs inside left-align div:",
    len(radio_section_inputs)
)
# Find input elements that are direct children of their parent
direct_inputs = driver.find_elements(
    By.CSS_SELECTOR,
    "input"
)

print(
    "Input elements found:",
    len(direct_inputs)
)
driver.quit()