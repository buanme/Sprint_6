from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # метод прокручивает страницу до локатора
    def scroll_page_to(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*locator))
        self.wait_to_visibility(locator)

    # метод кликает по элементу
    def click_to(self, locator):
        self.wait_to_clickable(locator)
        self.driver.find_element(*locator).click()

    # метод ожидания загрузки элемента
    def wait_to_visibility(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    # метод ожидания кликабельности элемента
    def wait_to_clickable(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator))

    # метод ожидания загрузки страницы
    def wait_to_url(self, url):
        self.wait.until(EC.url_to_be(url))

    # метод чтения текста
    def read_text(self, locator):
        return self.driver.find_element(*locator).text

    # метод переключает вкладку
    def switch_to(self, page):
        return self.driver.switch_to.window(self.driver.window_handles[page])

    # метод заполнения поля
    def fill(self, locator, key):
        self.driver.find_element(*locator).send_keys(key)
