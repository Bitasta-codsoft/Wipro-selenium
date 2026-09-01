from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

driver.maximize_window()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
# 1. By.ID
name = driver.find_element(By.ID, "name")
print("Name field found:", name.is_displayed())


# 2. By.NAME
radio_buttons = driver.find_elements(
    By.NAME, "radioButton"
)
print("Radio buttons found:", len(radio_buttons))


# 3. By.TAG_NAME
links = driver.find_elements(By.TAG_NAME, "a")
print("Total links:", len(links))


# 4. By.LINK_TEXT
open_tab = driver.find_element(
    By.LINK_TEXT, "Open Tab"
)
print("Open Tab link found:", open_tab.is_displayed())


# 5. By.CLASS_NAME
practice_button = driver.find_element(
    By.CLASS_NAME, "btn-style"
)
print("Button found:", practice_button.is_displayed())
time.sleep(2)
driver.quit()