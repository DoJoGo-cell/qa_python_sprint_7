import pytest
import generators
from api_client import CourierAPI, OrderAPI

@pytest.fixture(scope='function')
def register_new_courier_and_autharization_and_return_data():

    login = generators.generate_random_string(10)
    password = generators.generate_random_string(10)
    first_name = generators.generate_random_string(10)


    create_payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    create_result = CourierAPI.create(create_payload)

    if create_result.status_code != 201:
        return None

    login_payload = {
        "login": login,
        "password": password,
    }

    auth_result = CourierAPI.login(login_payload)

    if auth_result.status_code != 200:
        return None
    
    courier_id = auth_result.json()["id"]
    
    yield create_payload, create_result.status_code, create_result.json(), auth_result.status_code, auth_result.json(), courier_id

    response = CourierAPI.delete(courier_id)
    print(f"Курьер {courier_id} удалён, статус: {response.status_code}")
    

@pytest.fixture(scope='function')
def creating_template_for_order_and_return_data():

    order_payload = {
        "firstName": generators.generate_random_string(10),
        "lastName": generators.generate_random_string(10),
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": None
    }

    yield order_payload

@pytest.fixture(scope='function')
def order_cancel():

    track = {}
    
    def schedule_cancel(order_track):
        track["value"] = order_track
    
    yield schedule_cancel
    
    if track["value"]:
        response = OrderAPI.cancel(track["value"])
        print(f"Заказ {track['value']} удалён, статус: {response.status_code}")