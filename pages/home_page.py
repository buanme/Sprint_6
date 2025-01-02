import allure
from selenium.webdriver.common.by import By

from locators.base_locators import BaseLocators
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
from urls import Urls


class HomePage(BasePage):

    @allure.step("Нажимаем верхнюю кнопку 'Заказать'")
    def order_upper(self):
        self.click_to((By.XPATH, BaseLocators.BUTTON_ORDER_UPPER))
        self.wait_to_visibility((By.CLASS_NAME, BaseLocators.FORM_ORDER_PART_I))

    @allure.step("Нажимаем нижнюю кнопку 'Заказать'")
    def order_low(self):
        self.scroll_page_to((By.XPATH, HomePageLocators.BUTTON_ORDER_LOW))
        self.click_to((By.XPATH, HomePageLocators.BUTTON_ORDER_LOW))

    @allure.step("Нажимаем на логотип 'Самокат'")
    def click_logo_samokat(self):
        self.click_to((By.CLASS_NAME, BaseLocators.LOGO_SAMOKAT))
        self.wait_to_url(Urls.MAIN_PAGE)

    @allure.step("Нажимаем на логотип 'Яндекс'")
    def click_logo_yandex(self):
        self.click_to((By.CLASS_NAME, BaseLocators.LOGO_YANDEX))
        self.switch_to(1)
        self.wait_to_url(Urls.DZEN_PAGE)

    @allure.step("Прокручиваем страницу вниз к вопросам")
    def scroll_page_down(self):
        self.scroll_page_to((By.CLASS_NAME, HomePageLocators.FORM_WITH_QUESTIONS))

    @allure.step("Кликаем по вопросу")
    def click_question(self, number_questions):
        self.click_to((By.ID, self.get_question(number_questions)))

    @allure.step("Читаем ответ на вопрос")
    def read_answer_value(self, number_questions):
        self.wait_to_visibility((By.XPATH, self.get_answer(number_questions)))
        return self.read_text((By.XPATH, self.get_answer(number_questions)))

    @allure.step("Выбираем вопрос")
    def get_question(self, number_questions):
        return HomePageLocators.QUESTION_LOCATOR.format(number_questions)

    @allure.step("Выбираем ответ")
    def get_answer(self, number_questions):
        return HomePageLocators.ANSWER_LOCATOR.format(number_questions)
