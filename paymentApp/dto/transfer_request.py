class TransferRequest:

    def __init__(self, amount, description, bank_name, account_number, reference):
        self._amount = amount
        self._bank_name = bank_name
        self._account_number = account_number
        self._reference = reference
        self._description = description

    def set_amount(self, amount):
        self._amount = amount




    def set_bank_name(self, bank_name):
        self._bank_name = bank_name

    def set_account_number(self, account_number):
        self._account_number = account_number

    def set_reference(self, reference):
        self._reference = reference

    def set_description(self, description):
        self._description = description

    def get_amount(self):
        return self._amount

    def get_bank_name(self):
        return self._bank_name

    def get_account_number(self):
        return self._account_number

    def get_reference(self):
        return self._reference

    def get_description(self):
        return self._description

