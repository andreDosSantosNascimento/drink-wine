class WrongTypeError(Exception):
    def __init__(self, key, type):
        self.message = {"error": f"{key} is expected to be of type {type}"}

class CityNotRegisteredError(Exception):
    def __init__(self):
        self.message = {"error": "City not registered."}

class InvalidError(Exception):
    def __init__(self, this):
        self.message = {"error": f"This {this} is not valid."}

class WrongNumberFormatError(Exception):
    def __init__(self):
        self.message = {"error": "Invalid phone number, only numbers expected!"}
        
class InvalidEmailError(Exception):
    def __init__(self):
        self.message = {"error": "This email is not valid."}

class AlreadyRegisteredError(Exception):
    def __init__(self, this):
        self.message = {"error": f"{this} already registered!"}

class NotFound(Exception):
    def __init__(self, this = ""):
        self.message = {"error": f"{this}Not found!"}

class WrongKeysError(Exception):
    def __init__(self, wrong_keys):
        self.message = {"wrong_keys": wrong_keys}


class MissingKeyError(Exception):
    def __init__(self, missing_keys):
        self.message = {"missing_keys": missing_keys}
