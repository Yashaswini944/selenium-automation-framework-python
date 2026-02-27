from pages.login_page import LoginPage

def test_valid_login(driver):
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url

def test_invalid_login(driver):
    login = LoginPage(driver)
    login.login("wrong_user", "wrong_pass")
    assert "Epic sadface" in login.get_error_message()
