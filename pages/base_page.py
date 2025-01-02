import allure
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    @allure.step("Прокручиваем страницу до локатора")
    def scroll_page_to(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*locator))
        self.wait_to_visibility(locator)

    @allure.step("Кликаемпо элементу")
    def click_to(self, locator):
        self.wait_to_clickable(locator)
        self.driver.find_element(*locator).click()

    @allure.step("Ожидаем загрузки элемента")
    def wait_to_visibility(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидаем кликабельности элемента")
    def wait_to_clickable(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Ожидаем загрузки страницы")
    def wait_to_url(self, url):
        self.wait.until(EC.url_to_be(url))

    @allure.step("Читаем текст")
    def read_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step("Переключаем вкладку")
    def switch_to(self, page):
        return self.driver.switch_to.window(self.driver.window_handles[page])

    @allure.step("Заполняем поле")
    def fill(self, locator, key):
        self.driver.find_element(*locator).send_keys(key)
