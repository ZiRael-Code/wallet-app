class FindBankRequest:

    def __init__(self, bank_name):
        self._bank_name = bank_name

    def set_bank_name(self, bank_name):
        self._bank_name = bank_name

    def get_bank_name(self):
        return self._bank_name
