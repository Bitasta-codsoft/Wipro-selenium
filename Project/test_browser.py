from selenium import webdriver

def test_open_browser():
    driver = webdriver.Chrome()

    driver.get("https://tutorialsninja.com/demo/")

    print(driver.title)

    driver.quit()