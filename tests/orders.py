import pytest
from selenium.webdriver.common.by import By


class Orders:

    # Проверить, что появилось всплывающее окно с сообщением об успешном создании заказа.
    @pytest.mark.parametrize("data, method",
                             [({'name': 'Заказ',
                               'last_name': 'Тестовый',
                               'adres': 'Москва',
                               'station': 'Бабушкинская',
                               'number': '79991234567',
                               'when': '25.11.2025',
                               'rental_period': 'сутки'}, 'upper'),
                                ({'name': 'Чайка',
                               'last_name': 'Ливингстон',
                               'adres': 'Москва',
                               'station': 'Аэропорт',
                               'number': '79995552299',
                               'when': '13.10.2025',
                               'rental_period': 'двое суток'}, 'low')
                              ])
    def test_check_order(self, home_page, order, data, method):
        if method == 'upper':
            home_page.order_upper()
        else:
            home_page.order_low()
        order.input_form_order(data)
        assert 'Заказ оформлен' in order.get_order_status()

    # Проверить: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».
    def test_check_logo_samokat(self, driver, home_page):
        home_page.order_upper()
        home_page.click_logo_samokat()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"

    # Проверить: если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.
    def test_check_logo_yandex(self, driver, home_page):
        home_page.click_logo_yandex()
        assert driver.current_url == "https://dzen.ru/?yredirect=true"
