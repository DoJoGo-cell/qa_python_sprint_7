class CoruierCreatingData:

    MISSING_LOGIN = {
        "password": "12345",
        "firstName": "sadasd"
    }

    MISSING_PASSWORD = {
        "login": "sadasd",
        "firstName": "sadasd"
    }

class CoruierLoginData:

    INVALID_DATA = {
        "login": "_ +%$",
        "password": "%&- "
    }

    MISSING_LOGIN = {
        "password": "12345"
    }

    MISSING_PASSWORD = {
        "login": "sadasd"
    }
