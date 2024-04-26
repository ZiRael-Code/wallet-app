class WalletNotExistException(ValueError):
    def __init__(self, message):
        self._message = message
        super().__init__(message)

    def get_message(self):
        return self._message
