import pytest

from urls.urls import Urls


class TestOrders:

    # Проверить, что появилось всплывающее окно с сообщением об успешном создании заказа.
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
    def test_check_order(self, base_page, home_page, order_page, data, method):
        if method == 'upper':
            base_page.order_upper()
        else:
            home_page.order_low()
        order_page.input_form_order(data)
        assert 'Заказ оформлен' in order_page.get_order_status()

    # Проверить: если нажать на логотип «Самоката», попадёшь на главную страницу «Самоката».
    def test_check_logo_samokat(self, driver, base_page):
        base_page.order_upper()
        base_page.click_logo_samokat()
        assert driver.current_url == Urls.MAIN_PAGE

    # Проверить: если нажать на логотип Яндекса, в новом окне через редирект откроется главная страница Дзена.
    def test_check_logo_yandex(self, driver, base_page):
        base_page.click_logo_yandex()
        assert driver.current_url == Urls.DZEN_PAGE
