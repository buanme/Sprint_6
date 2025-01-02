import allure
import pytest

from urls import Urls


class TestOrders:

    @allure.title("Проверка, что появляется всплывающее окно с сообщением об успешном создании заказа.")
    @pytest.mark.parametrize("data, method",
                             [({'name': 'Заказ',
                               'last_name': 'Тестовый',
                               'address': 'Москва',
                               'station': 'Бабушкинская',
                               'number': '79991234567',
                               'when': '25.11.2025',
                               'rental_period': 'сутки'}, 'upper'),
                                ({'name': 'Чайка',
                               'last_name': 'Ливингстон',
                               'address': 'Москва',
                               'station': 'Аэропорт',
                               'number': '79995552299',
                               'when': '13.10.2025',
                               'rental_period': 'двое суток'}, 'low')
                              ])
    def test_check_order(self, home_page, order_page, data, method):
        if method == 'upper':
            home_page.order_upper()
        else:
            home_page.order_low()
        order_page.input_form_order(data)
        assert 'Заказ оформлен' in order_page.get_order_status()

    @allure.title("Проверка, что при нажатии на логотип «Самоката», попадёшь на главную страницу «Самоката».")
    def test_check_logo_samokat(self, driver, home_page):
        home_page.order_upper()
        home_page.click_logo_samokat()
        assert driver.current_url == Urls.MAIN_PAGE

    @allure.title("Проверка, что при нажатии на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.")
    def test_check_logo_yandex(self, driver, home_page):
        home_page.click_logo_yandex()
        assert driver.current_url == Urls.DZEN_PAGE
