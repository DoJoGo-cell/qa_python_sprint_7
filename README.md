# qa_python_7 - Тестирование API сервиса Яндекс Самокат

Автоматизированные тесты для API сайта [Яндекс Самокат](https://qa-scooter.praktikum-services.ru/).
Документация API [Доументация](https://qa-scooter.praktikum-services.ru/docs/)
Проект проверяет следующие ручки API:
- Создание курьера
- Авторизация курьера
- Создание заказа
- Получение списка заказов

## Реализованные тесты (22 тестов):

### 1-8. Тесты создания курьера
- `test_courier_creating_valid_data_created` — проверка успешного создания курьера используя валидные генеративные данные
- `test_courier_creating_valid_data_status_code_created` — проверка возврата правильного статус кода при успешном создании курьера
- `test_courier_creating_valid_data_return_message_created` — проверка возврата правильного сообщения в теле ответа при успешном создании курьера
- `test_courier_creating_duplicate_data_conflict` — проверка невозможности создания двух курьеров с идентичными данными
- `test_courier_creating_duplicate_data_return_message_conflict` — проверка возврата правильного сообщения об ошибке в теле ответа при неудачной попытке создания двух идентичных курьеров
- `test_courier_creating_missing_required_field_bad_request` — проверка невозможности создания курьера при незаполненности обязательных полей запроса
- `test_courier_creating_missing_required_field_return_message_bad_request[missing_data0]` — проверка возврата правильного сообщения об ошибке в теле ответа при незаполненности обязательного поля запроса login
- `test_courier_creating_missing_required_field_return_message_bad_request[missing_data1]` — проверка возврата правильного сообщения об ошибке в теле ответа при незаполненности обязательного поля запроса password

### 9-13. Тесты авторизации курьера
- `test_courier_login_valid_data_success` — проверка успешной авторизации курьера используя валидные генеративные данные
- `test_courier_login_valid_data_return_message_success` — проверка возврата правильного сообщения в теле ответа при успешной авторизации курьера
- `test_courier_login_invalid_data_return_message_not_found` — проверка возврата правильного сообщения об ошибке в теле ответа при неудачной попытке авторизации несуществующего курьера
- `test_courier_login_missing_required_field_return_message_bad_request[missing_data0]` — проверка возврата правильного сообщения об ошибке в теле ответа при незаполненности обязательного поля запроса login
- `test_courier_login_missing_required_field_return_message_bad_request[missing_data1]` — проверка возврата правильного сообщения об ошибке в теле ответа при незаполненности обязательного поля запроса password

### 14. Тест Получения списка заказов
- `test_getting_order_list_success` — проверка успешного получения списка заказов без использования необязательных параметров в запросе

### 15-22. Создание заказа
- `test_creating_order_with_any_colour_created[creating_order_with_different_colors_and_return_data0]` — проверка успешного создания заказа с параметром цвета "BLACK"
- `test_creating_order_with_any_colour_created[creating_order_with_different_colors_and_return_data1]` — проверка успешного создания заказа с параметром цвета "GRAY"
- `test_creating_order_with_any_colour_created[creating_order_with_different_colors_and_return_data2]` — проверка успешного создания заказа с параметрами цвета "BLACK" и"GRAY"
- `test_creating_order_with_any_colour_created[creating_order_with_different_colors_and_return_data3]` — проверка успешного создания заказа с пустым параметром цвета ""
- `test_creating_order_with_any_colour_return_message_success[creating_order_with_different_colors_and_return_data0]` — проверка возврата правильного сообщения в теле ответа при успешном создании заказа с параметром цвета "BLACK"
- `test_creating_order_with_any_colour_return_message_success[creating_order_with_different_colors_and_return_data1]` — проверка возврата правильного сообщения в теле ответа при успешном создании заказа с параметром цвета "GRAY"
- `test_creating_order_with_any_colour_return_message_success[creating_order_with_different_colors_and_return_data2]` — проверка возврата правильного сообщения в теле ответа при успешном создании заказа с параметрами цвета "BLACK" и"GRAY"
- `test_creating_order_with_any_colour_return_message_success[creating_order_with_different_colors_and_return_data3]` — проверка возврата правильного сообщения в теле ответа при успешном создании заказа с пустым параметром цвета ""

## Установить зависимости
pip install -r requirements.txt

## Запуск тестов
pytest -v -s tests/

## Просмотр Allure отчета
allure open allure_report

## Результат
6 failed, 16 passed in 56.53s
