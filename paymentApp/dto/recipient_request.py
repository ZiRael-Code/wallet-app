class RecipientRequest:
    def __init__(self, bank_name, account_number):
        self.account_number = account_number
        self.bank_name = bank_name

    def set_bank_name(self, bank_name):
        self.bank_name = bank_name

    def get_bank_name(self):
        return self.bank_name

    def set_account_number(self, account_number):
        self.account_number = account_number

    def get_account_number(self):
        return self.account_number
