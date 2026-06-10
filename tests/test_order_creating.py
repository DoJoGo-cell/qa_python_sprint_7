import allure
from constants import StatusCodes

@allure.feature('Создание заказа')
class TestOrderCreating:

    @allure.title('Успешное создание заказа с разными параметрами цвета')
    @allure.description('Тест проверяет успешное создание заказа с параметрами цвета: "BLACK", "GRAY", ["BLACK", "GRAY"], ""')
    def test_creating_order_with_any_colour_created(self, creating_order_with_different_colors_and_return_data):
        with allure.step('Создание заказа'):
            order = creating_order_with_different_colors_and_return_data
            status_code = order[0]

        with allure.step(f'Проверка возврата статус кода - {StatusCodes.CREATED} и сообщения с track заказа'):
            assert status_code == StatusCodes.CREATED

    @allure.title('Возврат track заказа в сообщении об успешном заказе')
    @allure.description('Тест проверяет возврат track заказа в теле ответа на запрос с параметрами цвета: "BLACK", "GRAY", ["BLACK", "GRAY"], ""')
    def test_creating_order_with_any_colour_return_message_success(self, creating_order_with_different_colors_and_return_data):
        with allure.step('Создание заказа'):
            order = creating_order_with_different_colors_and_return_data
            track = order[1]

        with allure.step('Проверка возврата сообщения с track заказа'):
            assert "track" in track and type(track["track"]) == int

