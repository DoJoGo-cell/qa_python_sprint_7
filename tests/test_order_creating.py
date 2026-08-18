import allure
import pytest
from constants import StatusCodes
from api_client import  OrderAPI

@allure.feature('Создание заказа')
class TestOrderCreating:

    @allure.title('Успешное создание заказа с разными параметрами цвета')
    @allure.description('Тест проверяет успешное создание заказа с параметрами цвета: ["BLACK"], ["GRAY"], ["BLACK", "GRAY"], [""]')
    @pytest.mark.parametrize('color', [
        ["BLACK"],
        ["GRAY"],
        ["BLACK", "GRAY"],
        [""]
    ])
    def test_creating_order_with_any_colour_created(self, color, creating_template_for_order_and_return_data, order_cancel):
        with allure.step(f'Заполнение шаблона недостающим параметром цвета - {color}'):
            payload = creating_template_for_order_and_return_data
            payload["color"] = color

        with allure.step('Создание заказа'):
            response = OrderAPI.order(payload)
            status_code = response.status_code
            track_id = response.json()

        with allure.step('Отмена заказа'):
            order_cancel(track_id)
            
        with allure.step(f'Проверка возврата статус кода - {StatusCodes.CREATED}'):
            assert status_code == StatusCodes.CREATED

    @allure.title('Возврат track заказа в сообщении об успешном заказе')
    @allure.description('Тест проверяет возврат track заказа в теле ответа на запрос с параметром цвета: ["BLACK"], ["GRAY"], ["BLACK", "GRAY"], [""]')
    @pytest.mark.parametrize('color', [
        ["BLACK"],
        ["GRAY"],
        ["BLACK", "GRAY"],
        [""]
    ])
    def test_creating_order_with_any_colour_return_message_success(self, color, creating_template_for_order_and_return_data, order_cancel):
        with allure.step(f'Заполнение шаблона недостающим параметром цвета - {color}'):
            payload = creating_template_for_order_and_return_data
            payload["color"] = color

        with allure.step('Создание заказа'):
            response = OrderAPI.order(payload)
            track_id = response.json()

        with allure.step('Отмена заказа'):
            order_cancel(track_id)
            
        with allure.step('Проверка возврата сообщения с track заказа'):
            assert "track" in track_id and type(track_id["track"]) == int
