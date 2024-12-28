class OrderPageLocators:

    # поле Имя
    NAME = "//div[@class='Input_InputContainer__3NykH']/input[@placeholder='* Имя']"

    # поле Фамилия
    LAST_NAME = "//div[@class='Input_InputContainer__3NykH']/input[@placeholder='* Фамилия']"

    # поле Адрес
    ADDRESS = "//div[@class='Input_InputContainer__3NykH']/input[@placeholder='* Адрес: куда привезти заказ']"

    # поле Станция метро
    STATION = "//div[@class='select-search']//input[@placeholder='* Станция метро']"

    # поле Телефон
    NUMBER = "//div[@class='Input_InputContainer__3NykH']/input[@placeholder='* Телефон: на него позвонит курьер']"

    # кнопка Далее
    BUTTON_NEXT_STEP = "//button[text()='Далее']"

    # форма Про аренду
    FORM_PRO_ARENDU = "Order_Header__BZXOb"

    # поле Когда
    WHEN = "//div[@class='Order_MixedDatePicker__3qiay']//input"

    # поле Срок аренды
    RENTAL_PERIOD = "//div[@class='Dropdown-placeholder']"

    # список Сроков аренды
    LIST_RENTAL_PERIODS = "//div[@class='Dropdown-menu']"

    # кнопка Заказать
    BUTTON_ORDER = "//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']"

    # окно подтверждения заказа
    WINDOW_CONFIRM_ORDER = "//div[@class='Order_Modal__YZ-d3']/div[text()='Хотите оформить заказ?']"

    # кнопка Да
    BUTTON_YES = "//div[@class='Order_Buttons__1xGrp']/button[text()='Да']"

    # окно созданного заказа
    WINDOW_CREAT_ORDER = "//div[@class='Order_Modal__YZ-d3']/div[text()='Заказ оформлен']"

    # список Станций метро
    @staticmethod
    def get_list_stations(station):
        return f"//div[contains(@class, 'select-search')]//div[text()='{station}']"

    # выбранный Срок аренды
    @staticmethod
    def select_rental_period(rental_period):
        return f"//div[@class='Dropdown-menu']/div[text()='{rental_period}']"