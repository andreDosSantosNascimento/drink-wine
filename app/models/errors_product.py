class InvalidValueuError(Exception):
    def __init__(self):
        self.message = {'error': 'the value passed in the VALUE field is not valid!'}


class InvalidOrderDateError(Exception):
    def __init__(self):
        self.message = {'error': 'Expiration date  must have format YYYY/MM/DD'}
