import requests 
from urls import URLs

class CourierAPI:

    @staticmethod
    def create(payload):
        response = requests.post(URLs.COURIER_CREATION, json=payload, timeout=10)
        return response
    
    @staticmethod
    def login(payload):
        response = requests.post(URLs.COURIER_LOGIN, json=payload, timeout=10)
        return response

    @staticmethod
    def delete(courier_id):
        response = requests.delete(f'{URLs.COURIER_DELETE}/{courier_id}')
        return response
    
class OrderAPI:

    @staticmethod
    def order(payload):
        response = requests.post(URLs.CREATING_ORDER, json=payload, timeout=10)
        return response
    
    @staticmethod
    def cancel(payload):
        response = requests.put(URLs.CANCEL_ORDER, params=payload)
        return response

    @staticmethod
    def order_list():
        response = requests.get(URLs.ORDER_LIST)
        return response
