### Selenium Automation Framework (Python · Selenium WebDriver · Pytest · POM)

A clean, modular, and maintainable UI Automation Framework built using Python, Selenium WebDriver, Pytest, and the Page Object Model (POM).
This framework demonstrates real‑world automation engineering practices such as reusable page objects, centralized driver setup, structured test execution, and HTML reporting.

### Framework Overview

This project automates UI test scenarios for the application https://www.saucedemo.com/ using a structured and scalable approach.
The framework is designed to be simple, readable, and extendable — suitable for both small and growing test suites.

### Key Features

Python + Selenium WebDriver for browser automation

Pytest as the test runner

Page Object Model (POM) for clean separation of UI actions

Centralized WebDriver setup using Pytest fixtures

HTML test reports generated via pytest-html

Organized folder structure for easy maintenance

Supports adding more pages, tests, and utilities without refactoring

### Page Object Model (POM)

Each page class contains:

Element locators

Page actions (methods)

Assertions/validations

This ensures:

Cleaner test scripts

Reusable UI actions

Easier maintenance when UI changes

### WebDriver Setup (Pytest Fixture)

The conftest.py file manages:

Browser initialization

Window maximization

Base URL navigation

Cleanup after test execution

This ensures consistent browser behavior across all tests.

### Sample Test Case

def test_valid_login(driver):

    login = LoginPage(driver)
    
    login.enter_username("standard_user")
    
    login.enter_password("secret_sauce")
    
    login.click_login()
    
    home = HomePage(driver)
    
    assert home.is_logged_in()


