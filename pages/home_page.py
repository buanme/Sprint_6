from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from locators.home_page_locators import HomePageLocators


class HomePage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # метод нажимает нижнюю кнопку "Заказать"
    def order_low(self):
        self.scroll_page_down()
        self.driver.find_element(By.XPATH, HomePageLocators.BUTTON_ORDER_LOW).click()

    # метод прокручивает страницу вниз к вопросам
    def scroll_page_down(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(By.CLASS_NAME, HomePageLocators.FORM_IMPORTANT_QUESTIONS))
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, HomePageLocators.FORM_WITH_QUESTIONS)))

    # метод кликает по вопросу
    def click_question(self, number_questions):
        self.driver.find_element(By.ID, HomePageLocators.get_question(number_questions)).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, HomePageLocators.get_answer(number_questions))))

    # метод читает ответ на вопрос
    def read_answer_value(self, number_questions):
        return self.driver.find_element(By.XPATH, HomePageLocators.get_answer(number_questions)).text
