import os


def take_screenshot(driver, name):
    os.makedirs("screenshots", exist_ok=True)

    file_path = os.path.join(
        "screenshots",
        f"{name}.png"
    )

    driver.save_screenshot(file_path)

    return file_path
