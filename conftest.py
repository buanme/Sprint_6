import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pages.home_page import HomePage
from pages.order_page import Order


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 40)


@pytest.fixture
def home_page(driver, wait):
    home_page = HomePage(driver, wait)
    return home_page


@pytest.fixture
def order(driver, wait):
    order = Order(driver, wait)
    return order

