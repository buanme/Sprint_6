from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    # Метод заполняет поле Имя
    def fill_name(self, name):
        self.fill((By.XPATH, OrderPageLocators.NAME), name)

    # Метод заполняет поле Фамилия
    def fill_last_name(self, last_name):
        self.fill((By.XPATH, OrderPageLocators.LAST_NAME), last_name)

    # Метод заполняет поле Адрес
    def fill_address(self, address):
        self.fill((By.XPATH, OrderPageLocators.ADDRESS), address)

    # Метод заполняет поле Станция метро
    def fill_station(self, station):
        self.fill((By.XPATH, OrderPageLocators.STATION), station)
        self.click_to((By.XPATH, self.get_list_stations(station)))

    # Метод заполняет поле Телефон
    def fill_number(self, number):
        self.fill((By.XPATH, OrderPageLocators.NUMBER), number)

    # Метод нажимает кнопку Далее в форме заказа
    def click_button_next_step(self):
        self.click_to((By.XPATH, OrderPageLocators.BUTTON_NEXT_STEP))
        self.wait_to_visibility((By.CLASS_NAME, OrderPageLocators.FORM_PRO_ARENDU))

    # Метод заполняет поле Когда
    def fill_when(self, when):
        self.fill((By.XPATH, OrderPageLocators.WHEN), when)
        self.fill((By.XPATH, OrderPageLocators.WHEN), Keys.RETURN)

    # Метод заполняет поле Срок аренды
    def fill_rental_period(self, rental_period):
        self.click_to((By.XPATH, OrderPageLocators.RENTAL_PERIOD))
        self.wait_to_clickable((By.XPATH, OrderPageLocators.LIST_RENTAL_PERIODS))
        self.click_to((By.XPATH, self.select_rental_period(rental_period)))

    # Метод нажимает кнопку Заказать
    def click_button_order(self):
        self.click_to((By.XPATH, OrderPageLocators.BUTTON_ORDER))
        self.wait_to_visibility((By.XPATH, OrderPageLocators.WINDOW_CONFIRM_ORDER))

    # Метод нажимает кнопку Да
    def click_confirm_button(self):
        self.click_to((By.XPATH, OrderPageLocators.BUTTON_YES))
        self.wait_to_visibility((By.XPATH, OrderPageLocators.WINDOW_CREAT_ORDER))

    # Метод заполняет форму заказа
    def input_form_order(self, data):
        self.fill_name(data['name'])
        self.fill_last_name(data['last_name'])
        self.fill_address(data['address'])
        self.fill_station(data['station'])
        self.fill_number(data['number'])
        self.click_button_next_step()
        self.fill_when(data['when'])
        self.fill_rental_period(data['rental_period'])
        self.click_button_order()
        self.click_confirm_button()

    # Метод получет инфо о статусе заказа
    def get_order_status(self):
        return self.read_text((By.XPATH, OrderPageLocators.WINDOW_CREAT_ORDER))

    # список Станций метро
    def get_list_stations(self, station):
        return f"//div[contains(@class, 'select-search')]//div[text()='{station}']"

    # выбранный Срок аренды
    def select_rental_period(self, rental_period):
        return f"//div[@class='Dropdown-menu']/div[text()='{rental_period}']"

