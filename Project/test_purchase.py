import json

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from utils.screenshot import take_screenshot
from utils.alert_handler import handle_alert


def test_purchase_product(driver):

    # Read test data
    with open("test_data/testdata_local.json", "r") as file:
        data = json.load(file)

    # Open website
    driver.get(data["url"])

    # Open My Account menu
    driver.find_element(
        "css selector", "a[title='My Account']"
    ).click()

    # Click Login
    driver.find_element(
        "link text", "Login"
    ).click()

    # Login
    login_page = LoginPage(driver)
    login_page.login(data["email"], data["password"])

    # Take screenshot after login
    take_screenshot(driver, "after_login")

    # Search for product
    home_page = HomePage(driver)
    home_page.search_product(data["product"])

    # Click on MacBook product
    driver.find_element(
        "link text", "MacBook"
    ).click()

    # Add product to cart
    driver.find_element(
        "id", "button-cart"
    ).click()

    # Handle alert if one appears
    handle_alert(driver)

    # Open cart
    driver.find_element(
        "css selector", "a[href*='checkout/cart']"
    ).click()

    # Update quantity
    cart_page = CartPage(driver)
    cart_page.update_quantity(data["quantity"])

    # Verify quantity
    actual_quantity = cart_page.get_quantity()

    assert actual_quantity == str(data["quantity"])

    # Take screenshot of cart
    take_screenshot(driver, "cart_quantity_2")