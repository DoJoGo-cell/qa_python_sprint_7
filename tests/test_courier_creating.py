import pytest
import allure
from constants import StatusCodes, CourierCreationMessages
from api_client import CourierAPI
from data import CoruierCreatingData


@allure.feature('Создание курьера')
class TestCourierCreating:

    @allure.title('Успешное создание курьера используя валидные генеративные данные')
    @allure.description('Тест проверяет успешное создание курьера используя валдиные генеративные данные при заполненности всех обязательных полей')
    def test_courier_creating_valid_data_created(self, register_new_courier_and_autharization_and_return_data):
        with allure.step('Создание и авторизация курьера'):
            courier = register_new_courier_and_autharization_and_return_data     

        with allure.step('Проверка создания курьера'):
            assert courier is not None

    @allure.title('Возврат правильного статус кода при успешном создании курьера')
    @allure.description('Тест проверяет возврат правильного статус кода при успешном создании курьера')
    def test_courier_creating_valid_data_status_code_created(self, register_new_courier_and_autharization_and_return_data):
        with allure.step('Создание и авторизация курьера'):
            courier = register_new_courier_and_autharization_and_return_data
            status_code = courier[1]

        with allure.step(f'Проверка возврата статус кода - {StatusCodes.CREATED}'):
            assert status_code == StatusCodes.CREATED

    @allure.title('Возврат правильного сообщения об успешном создании курьера')
    @allure.description('Тест проверяет возврат правильного сообщения об успешном создании курьера')
    def test_courier_creating_valid_data_return_message_created(self, register_new_courier_and_autharization_and_return_data):
        with allure.step('Создание и авторизация курьера'):
            courier = register_new_courier_and_autharization_and_return_data
            response = courier[2]

        with allure.step(f'Проверка возврата сообщения об успехе - {CourierCreationMessages.CREATED}'):
            assert response == CourierCreationMessages.CREATED

    @allure.title('Неудачная попытка создания двух одинаковых курьеров')
    @allure.description('Тест проверяет возврат правильного статус кода при неудачной попытке создания двух одинаковых курьеров')
    def test_courier_creating_duplicate_data_conflict(self, register_new_courier_and_autharization_and_return_data):
        with allure.step('Создание первого курьера'):
            courier = register_new_courier_and_autharization_and_return_data

            payload = courier[0]        
        
        with allure.step('Создание второго курьера используя данные при создании первого курьера'):
            response = CourierAPI.create(payload)

        with allure.step(f'Проверка возврата статус кода - {StatusCodes.CONFLICT}'):
            assert response.status_code == StatusCodes.CONFLICT

    @allure.title('Возврат сообщения об ошибке при попытке создания двух курьеров с одинаковыми логинами')
    @allure.description('Тест проверяет возврат правильного статус кода при неудачной попытке создания двух одинаковых курьеров')
    def test_courier_creating_duplicate_data_return_message_conflict(self, register_new_courier_and_autharization_and_return_data):
        with allure.step('Создание первого курьера'):
            courier = register_new_courier_and_autharization_and_return_data

            payload = courier[0]        
        
        with allure.step('Создание второго курьера используя данные при создании первого курьера'):
            response = CourierAPI.create(payload)

        with allure.step(f'Проверка возврата сообщения об ошибке - {CourierCreationMessages.CONFLICT}'):
            assert response.json() == CourierCreationMessages.CONFLICT

    @allure.title('Неудачная попытка создания курьера при незаполненности обязательного поля')
    @allure.description('Тест проверяет невозможность создания курьера если обязательное поле login не заполнено')
    def test_courier_creating_missing_required_field_bad_request(self):
        with allure.step('Создание и авторизация курьера'):
            payload = CoruierCreatingData.MISSING_LOGIN
            response = CourierAPI.create(payload)

        with allure.step(f'Проверка возврата статус кода - {StatusCodes.BAD_REQUEST}'):
            assert response.status_code == StatusCodes.BAD_REQUEST

    @allure.title('Возврат сообщения об ошибке при незаполненности обязательного поля')
    @allure.description('Тест проверяет возврат сообщения об ошибке если обязательное поле login или password не заполнено')
    @pytest.mark.parametrize('missing_data',[
        CoruierCreatingData.MISSING_LOGIN,
        CoruierCreatingData.MISSING_PASSWORD
    ])
    def test_courier_creating_missing_required_field_return_message_bad_request(self, missing_data):
        with allure.step('Создание и авторизация курьера'):
            payload = missing_data
            response = CourierAPI.create(payload)

        with allure.step(f'Проверка возврата сообщения об ошибке - {CourierCreationMessages.BAD_REQUEST}'):
            assert response.json() == CourierCreationMessages.BAD_REQUEST




        




        

