from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from locators.base_locators import BaseLocators
from urls.urls import Urls


class BasePage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # метод нажимает верхнюю кнопку "Заказать"
    def order_upper(self):
        self.driver.find_element(By.XPATH, BaseLocators.BUTTON_ORDER_UPPER).click()
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, BaseLocators.FORM_ORDER_PART_I)))

    # метод нажимает на логотип "Самокат"
    def click_logo_samokat(self):
        self.driver.find_element(By.CLASS_NAME, BaseLocators.LOGO_SAMOKAT).click()
        self.wait.until(EC.url_to_be(Urls.MAIN_PAGE))

    # метод нажимает на логотип "Яндекс"
    def click_logo_yandex(self):
        self.driver.find_element(By.CLASS_NAME, BaseLocators.LOGO_YANDEX).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait.until(EC.url_to_be(Urls.DZEN_PAGE))
