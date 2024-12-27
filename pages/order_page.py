from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Order:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # Метод заполняет поле Имя
    def fill_name(self, name):
        self.driver.find_element(By.XPATH, "//div[@class='Input_InputContainer__3NykH']/input[@placeholder='* Имя']").send_keys(name)

    # Метод заполняет поле Фамилия
    def fill_last_name(self, last_name):
        self.driver.find_element(By.XPATH, "//div[@class='Input_InputContainer__3NykH']/input[@placeholder='* Фамилия']").send_keys(last_name)

    # Метод заполняет поле Адрес
    def fill_adres(self, adres):
        self.driver.find_element(By.XPATH, "//div[@class='Input_InputContainer__3NykH']/input[@placeholder='* Адрес: куда привезти заказ']").send_keys(adres)

    # Метод заполняет поле Станция метро
    def fill_station(self, station):
        self.driver.find_element(By.XPATH, "//div[@class='select-search']//input[@placeholder='* Станция метро']").send_keys(station)
        self.wait.until(EC.presence_of_element_located((By.XPATH, f"//div[contains(@class, 'select-search')]//div[text()='{station}']"))).click()

    # Метод заполняет поле Телефон
    def fill_number(self, number):
        self.driver.find_element(By.XPATH, "//div[@class='Input_InputContainer__3NykH']/input[@placeholder='* Телефон: на него позвонит курьер']").send_keys(number)

    # Метод нажимает кнопку Далее в форме заказа
    def click_button_next_step(self):
        self.driver.find_element(By.XPATH, "//button[text()='Далее']").click()
        self.wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'Order_Header__BZXOb'), 'Про аренду'))

    # Метод заполняет поле Когда
    def fill_when(self, when):
        self.driver.find_element(By.XPATH, "//div[@class='Order_MixedDatePicker__3qiay']//input").send_keys(when)
        self.driver.find_element(By.XPATH, "//div[@class='Order_MixedDatePicker__3qiay']//input").send_keys(Keys.RETURN)

    # Метод заполняет поле Срок аренды
    def fill_rental_period(self, rental_period):
        self.driver.find_element(By.XPATH, "//div[@class='Dropdown-placeholder']").click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='Dropdown-menu']")))
        self.driver.find_element(By.XPATH, f"//div[@class='Dropdown-menu']/div[text()='{rental_period}']").click()

    # Метод нажимает кнопку Заказать
    def click_button_order(self):
        self.driver.find_element(By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']").click()
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'Order_Modal__YZ-d3')))

    # Метод нажимает кнопку Да
    def click_confirm_button(self):
        self.driver.find_element(By.XPATH, "//div[@class='Order_Buttons__1xGrp']/button[text()='Да']").click()
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'Order_Modal__YZ-d3')))

    # Метод заполняет форму заказа.
    def input_form_order(self, data):
        self.fill_name(data['name'])
        self.fill_last_name(data['last_name'])
        self.fill_adres(data['adres'])
        self.fill_station(data['station'])
        self.fill_number(data['number'])
        self.click_button_next_step()
        self.fill_when(data['when'])
        self.fill_rental_period(data['rental_period'])
        self.click_button_order()
        self.click_confirm_button()

    # получить статус заказа
    def get_order_status(self):
        return self.driver.find_element(By.CLASS_NAME, 'Order_Modal__YZ-d3').text
