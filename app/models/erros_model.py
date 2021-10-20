class WrongTypeError(Exception):
    def __init__(self, key, type):
        self.message = {"error": f"{key} is expected to be of type {type}"}

class CityNotRegisteredError(Exception):
    def __init__(self):
        self.message = {"error": "City not registered."}