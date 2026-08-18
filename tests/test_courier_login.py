import allure
import pytest
from constants import StatusCodes, CourierLoginMessages
from api_client import CourierAPI
from data import CoruierLoginData

@allure.feature('Авторизация курьера')
class TestCourierLogin:

    @allure.title('Успешное авторизация курьера')
    @allure.description('Тест проверяет успешную авторизацию курьера при заполненности всех обязательных полей')
    def test_courier_login_valid_data_success(self, register_new_courier_and_autharization_and_return_data):
        with allure.step('Создание и авторизация курьера'):
            courier = register_new_courier_and_autharization_and_return_data
            status_code = courier[3]

        with allure.step(f'Проверка возврата статус кода - {StatusCodes.OK}'):
            assert status_code == StatusCodes.OK

    @allure.title('Возврат id курьера в сообщении об успешной авторизации')
    @allure.description('Тест проверяет возврат id курьера в теле ответа на запрос')
    def test_courier_login_valid_data_return_message_success(self, register_new_courier_and_autharization_and_return_data):
        with allure.step('Создание курьера'):
            courier = register_new_courier_and_autharization_and_return_data
            result = courier[4]

        with allure.step('Проверка возврата сообщения с id курьера'):
            assert "id" in result and type(result["id"]) == int

    @allure.title('Неудачная попытка авторизации курьера при вводе в обязательные поля невалидных данных')
    @allure.description('Тест проверяет невозможность авторизации при вводе невалидных данных в обязательные поля login и password')
    def test_courier_login_invalid_data_not_found(self):
        with allure.step('Авторизация курьера с невалидными данными'):
            response = CourierAPI.login(CoruierLoginData.INVALID_DATA)

        with allure.step(f'Проверка возврата статус кода - {StatusCodes.NOT_FOUND}'):
            assert response.status_code == StatusCodes.NOT_FOUND

    @allure.title('Возврат собщения об ошибке при вводе в обязательные поля невалидных данных')
    @allure.description('Тест проверяет возврат сообщения об ошибке при вводе невалидных данных в обязательные поля login и password')
    def test_courier_login_invalid_data_return_message_not_found(self):
        with allure.step('Авторизация курьера с невалидными данными'):
            response = CourierAPI.login(CoruierLoginData.INVALID_DATA)

        with allure.step(f'Проверка возврата сообщения об ошибке - {CourierLoginMessages.NOT_FOUND}'):
            assert response.json() == CourierLoginMessages.NOT_FOUND

    @allure.title('Возврат сообщения об ошибке при незаполненности обязательного поля')
    @allure.description('Тест проверяет возврат сообщения об ошибке если обязательное поле login или password не заполнено')
    @pytest.mark.parametrize('missing_data',[
        CoruierLoginData.MISSING_LOGIN,
        CoruierLoginData.MISSING_PASSWORD
    ])
    def test_courier_login_missing_required_field_return_message_bad_request(self, missing_data):
        with allure.step('авторизация курьера'):
            payload = missing_data
            response = CourierAPI.login(payload)

        with allure.step(f'Проверка возврата сообщения об ошибке - {CourierLoginMessages.BAD_REQUEST}'):
            assert response.json() == CourierLoginMessages.BAD_REQUEST