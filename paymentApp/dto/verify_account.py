class VerifyAccountRequest:
    def __init__(self, bank_name, account_number):
        self.__bank_name = bank_name
        self.__account_number = account_number

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def set_bank_name(self, bank_name):
        self.__account_number = bank_name

    def get_account_number(self):
        return self.__account_number

    def get_bank_name(self):
        return self.__bank_name

