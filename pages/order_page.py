from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from locators.order_page_locators import OrderPageLocators


class OrderPage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Метод заполняет поле Имя
    def fill_name(self, name):
        self.driver.find_element(By.XPATH, OrderPageLocators.NAME).send_keys(name)

    # Метод заполняет поле Фамилия
    def fill_last_name(self, last_name):
        self.driver.find_element(By.XPATH, OrderPageLocators.LAST_NAME).send_keys(last_name)

    # Метод заполняет поле Адрес
    def fill_address(self, address):
        self.driver.find_element(By.XPATH, OrderPageLocators.ADDRESS).send_keys(address)

    # Метод заполняет поле Станция метро
    def fill_station(self, station):
        self.driver.find_element(By.XPATH, OrderPageLocators.STATION).send_keys(station)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, OrderPageLocators.get_list_stations(station)))).click()

    # Метод заполняет поле Телефон
    def fill_number(self, number):
        self.driver.find_element(By.XPATH, OrderPageLocators.NUMBER).send_keys(number)

    # Метод нажимает кнопку Далее в форме заказа
    def click_button_next_step(self):
        self.driver.find_element(By.XPATH, OrderPageLocators.BUTTON_NEXT_STEP).click()
        self.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, OrderPageLocators.FORM_PRO_ARENDU), 'Про аренду'))

    # Метод заполняет поле Когда
    def fill_when(self, when):
        self.driver.find_element(By.XPATH, OrderPageLocators.WHEN).send_keys(when)
        self.driver.find_element(By.XPATH, OrderPageLocators.WHEN).send_keys(Keys.RETURN)

    # Метод заполняет поле Срок аренды
    def fill_rental_period(self, rental_period):
        self.driver.find_element(By.XPATH, OrderPageLocators.RENTAL_PERIOD).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, OrderPageLocators.LIST_RENTAL_PERIODS)))
        self.driver.find_element(By.XPATH, OrderPageLocators.select_rental_period(rental_period)).click()

    # Метод нажимает кнопку Заказать
    def click_button_order(self):
        self.driver.find_element(By.XPATH, OrderPageLocators.BUTTON_ORDER).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, OrderPageLocators.WINDOW_CONFIRM_ORDER)))

    # Метод нажимает кнопку Да
    def click_confirm_button(self):
        self.driver.find_element(By.XPATH, OrderPageLocators.BUTTON_YES).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, OrderPageLocators.WINDOW_CREAT_ORDER)))

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
        return self.driver.find_element(By.XPATH, OrderPageLocators.WINDOW_CREAT_ORDER).text
