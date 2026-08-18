class StatusCodes:

    OK = 200
    CREATED = 201
    BAD_REQUEST = 400
    NOT_FOUND = 404
    CONFLICT = 409

class CourierCreationMessages:

    CREATED = {"ok": True}
    BAD_REQUEST = {"message": "Недостаточно данных для создания учетной записи"}
    CONFLICT = {"message": "Этот логин уже используется"}

class CourierLoginMessages:

    BAD_REQUEST = {"message":  "Недостаточно данных для входа"}
    NOT_FOUND = {"message": "Учетная запись не найдена"}


