class InvalidDetailsException(ValueError):
    def __init__(self, message):
        self._message = message
        super().__init__(self._message)

    def get_message(self):
        return self._message
