# Wipro Selenium Capstone Project

## Project Title
Automate a Web Application Using Selenium WebDriver with Python

## Overview

This project automates an e-commerce purchase workflow using Selenium WebDriver with Python and pytest.

The application used for automation is the TutorialsNinja OpenCart Demo.

## Technologies Used

- Python
- Selenium WebDriver
- Pytest
- pytest-html
- JSON
- HTML Reports
- Google Chrome

## Automated Test Scenario

The automation performs the following steps:

1. Launch the Chrome browser
2. Open the TutorialsNinja e-commerce website
3. Navigate to the Login page
4. Log in using test credentials
5. Search for a product
6. Select the MacBook product
7. Add the product to the cart
8. Open the shopping cart
9. Update the product quantity to 2
10. Verify the updated quantity
11. Capture screenshots
12. Generate an HTML execution report
13. Handle alerts/popups when present

## Project Structure

```text
Project/
├── pages/
├── reports/
├── screenshots/
├── test_data/
├── tests/
├── utils/
├── .gitignore
├── README.md
└── requirements.txt
