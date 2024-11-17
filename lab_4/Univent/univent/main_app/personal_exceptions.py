class InvalidException(Exception):
    def __init__(self):
        message = "Неверно заполнена форма"
        super().__init__(message)
