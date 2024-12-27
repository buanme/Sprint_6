from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # метод нажимает верхнюю кнопку "Заказать"
    def order_upper(self):
        self.driver.find_element(By.XPATH, "//div[@class='Header_Nav__AGCXC']/button[1]").click()
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'Order_Content__bmtHS')))

    # метод нажимает нижнюю кнопку "Заказать"
    def order_low(self):
        self.scroll_page_down()
        self.driver.find_element(By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button").click()

    # метод нажимает на логотип "Самокат"
    def click_logo_samokat(self):
        self.driver.find_element(By.CLASS_NAME, "Header_LogoScooter__3lsAR").click()
        self.wait.until(EC.url_to_be("https://qa-scooter.praktikum-services.ru/"))

    #
    def click_logo_yandex(self):
        self.driver.find_element(By.CLASS_NAME, "Header_LogoYandex__3TSOI").click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait.until(EC.url_to_be("https://dzen.ru/?yredirect=true"))

    # метод прокручивает страницу вниз к вопросам
    def scroll_page_down(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(By.CLASS_NAME, "Home_FourPart__1uthg"))
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "Home_FAQ__3uVm4")))

    # метод кликает по вопросу
    def click_question(self, number_questions):
        self.driver.find_element(By.ID, "accordion__heading-"+(str(number_questions))).click()
        self.wait.until(EC.visibility_of_element_located((By.ID, "accordion__panel-"+(str(number_questions)))))

    # метод читает ответ на вопрос
    def read_answer_value(self, number_questions):
        return self.driver.find_element(By.XPATH, "//div[@id='accordion__panel-"+(str(number_questions))+"']/p").text
