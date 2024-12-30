from selenium.webdriver.common.by import By

from locators.base_locators import BaseLocators
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
from urls import Urls


class HomePage(BasePage):

    # метод нажимает верхнюю кнопку "Заказать"
    def order_upper(self):
        self.click_to((By.XPATH, BaseLocators.BUTTON_ORDER_UPPER))
        self.wait_to_visibility((By.CLASS_NAME, BaseLocators.FORM_ORDER_PART_I))

    # метод нажимает нижнюю кнопку "Заказать"
    def order_low(self):
        self.scroll_page_to((By.XPATH, HomePageLocators.BUTTON_ORDER_LOW))
        self.click_to((By.XPATH, HomePageLocators.BUTTON_ORDER_LOW))

    # метод нажимает на логотип "Самокат"
    def click_logo_samokat(self):
        self.click_to((By.CLASS_NAME, BaseLocators.LOGO_SAMOKAT))
        self.wait_to_url(Urls.MAIN_PAGE)

    # метод нажимает на логотип "Яндекс"
    def click_logo_yandex(self):
        self.click_to((By.CLASS_NAME, BaseLocators.LOGO_YANDEX))
        self.switch_to(1)
        self.wait_to_url(Urls.DZEN_PAGE)

    # метод прокручивает страницу вниз к вопросам
    def scroll_page_down(self):
        self.scroll_page_to((By.CLASS_NAME, HomePageLocators.FORM_WITH_QUESTIONS))

    # метод кликает по вопросу
    def click_question(self, number_questions):
        self.click_to((By.ID, self.get_question(number_questions)))

    # метод читает ответ на вопрос
    def read_answer_value(self, number_questions):
        self.wait_to_visibility((By.XPATH, self.get_answer(number_questions)))
        return self.read_text((By.XPATH, self.get_answer(number_questions)))

    # поле с вопросом
    def get_question(self, number_questions):
        return "accordion__heading-"+(str(number_questions))

    # поле с ответом
    def get_answer(self, number_questions):
        return "//div[@id='accordion__panel-"+(str(number_questions))+"']/p"
