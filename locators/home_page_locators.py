class HomePageLocators:

    # нижняя кнопка Заказать
    BUTTON_ORDER_LOW = "//div[@class='Home_FinishButton__1_cWm']/button"

    # форма Вопросы о важном
    FORM_IMPORTANT_QUESTIONS = "Home_FourPart__1uthg"

    # форма с вопросами
    FORM_WITH_QUESTIONS = "Home_FAQ__3uVm4"

    # поле с вопросом
    @staticmethod
    def get_question(number_questions):
        return "accordion__heading-"+(str(number_questions))

    # поле с ответом
    @staticmethod
    def get_answer(number_questions):
        return "//div[@id='accordion__panel-"+(str(number_questions))+"']/p"
