import requests 
import allure
from urls import URLs

class CourierAPI:

    @staticmethod
    @allure.step(f"Создание курьера: POST {URLs.COURIER_CREATION}")
    def create(payload):
        response = requests.post(URLs.COURIER_CREATION, json=payload, timeout=10)
        return response
    
    @staticmethod
    @allure.step(f"Авторизация курьера: POST {URLs.COURIER_LOGIN}")
    def login(payload):
        response = requests.post(URLs.COURIER_LOGIN, json=payload, timeout=10)
        return response

    @staticmethod
    @allure.step(f"Удаление курьера: DELETE {URLs.COURIER_DELETE}")
    def delete(courier_id):
        response = requests.delete(f'{URLs.COURIER_DELETE}/{courier_id}')
        return response
    
class OrderAPI:

    @staticmethod
    @allure.step(f"Создание заказа: POST {URLs.CREATING_ORDER}")
    def order(payload):
        response = requests.post(URLs.CREATING_ORDER, json=payload, timeout=10)
        return response
    
    @staticmethod
    @allure.step(f"Отмена заказа: PUT {URLs.CANCEL_ORDER}")
    def cancel(payload):
        response = requests.put(URLs.CANCEL_ORDER, params=payload)
        return response

    @staticmethod
    @allure.step(f"Получение списка заказов: GET {URLs.ORDER_LIST}")
    def order_list():
        response = requests.get(URLs.ORDER_LIST)
        return response
