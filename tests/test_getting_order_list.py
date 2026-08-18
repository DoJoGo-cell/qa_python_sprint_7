import allure
from constants import StatusCodes
from api_client import OrderAPI

@allure.feature('Получение списка заказов')
class TestGettingOrderList:

    @allure.title('Успешное получение списка заказов')
    @allure.description('Тест проверяет успешное получение списка заказов без использования необязательных параметров')
    def test_getting_order_list_success(self):
        with allure.step('Получение списка заказов'):
            get_list = OrderAPI.order_list()
        
        with allure.step(f'Провека возвращаемого типа данных и статус кода - {StatusCodes.OK}'):
            assert type(get_list.json()["orders"]) == list and get_list.status_code == StatusCodes.OK