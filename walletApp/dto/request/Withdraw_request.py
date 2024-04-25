class WithdrawalRequest:
    def __init__(self, description, amount, bank_name, account_number, wallet_pin, email):
        self._description = description
        self._amount = amount
        self._bank_name = bank_name
        self._account_number = account_number
        self._wallet_pin = wallet_pin
        self.__email = email

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def set_amount(self, amount):
        self._amount = amount

    def set_description(self, description):
        self._description = description

    def set_bank_name(self, bank_name):
        self._bank_name = bank_name

    def set_account_number(self, account_number):
        self._account_number = account_number

    def set_wallet_pin(self, wallet_pin):
        self._wallet_pin = wallet_pin

    def get_amount(self):
        return self._amount

    def get_account_number(self):
        return self._account_number

    def get_bank_name(self):
        return self._bank_name

    def get_description(self):
        return self._description

    def get_wallet_pin(self):
        return self._wallet_pin
