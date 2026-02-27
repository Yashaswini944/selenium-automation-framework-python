import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    driver.get("https://www.saucedemo.com/")
    time.sleep(2)  # wait for DNS + page load

    yield driver
    driver.quit()
