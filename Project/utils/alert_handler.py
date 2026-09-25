from selenium.common.exceptions import NoAlertPresentException


def handle_alert(driver):
    try:
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        return alert_text

    except NoAlertPresentException:
        return None
