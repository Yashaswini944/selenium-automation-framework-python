from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

def test_add_to_cart(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    add_btn = (By.ID, "add-to-cart-sauce-labs-backpack")
    cart_icon = (By.CLASS_NAME, "shopping_cart_badge")

    driver.find_element(*add_btn).click()
    assert driver.find_element(*cart_icon).text == "1"
