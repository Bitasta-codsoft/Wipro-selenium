from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Find all links using TAG_NAME
links = driver.find_elements(By.TAG_NAME, "a")

print("\nLinks:")

for link in links:
    text = link.text.strip()

    if text:
        print(text)


# Find all checkboxes using XPATH
checkboxes = driver.find_elements(
    By.XPATH, "//input[@type='checkbox']"
)

print("\nCheckboxes:", len(checkboxes))
driver.quit()