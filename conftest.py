import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.order_page import OrderPage
from urls import Urls


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.MAIN_PAGE)
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 40)


@pytest.fixture
def base_page(driver, wait):
    base_page = BasePage(driver, wait)
    return base_page


@pytest.fixture
def home_page(driver, wait):
    home_page = HomePage(driver, wait)
    return home_page


@pytest.fixture
def order_page(driver, wait):
    order_page = OrderPage(driver, wait)
    return order_page

