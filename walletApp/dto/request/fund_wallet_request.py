class FundWalletRequest:
    def __init__(self, amount, email):
        self.__amount = amount
        self.__email = email

    def set_email(self, email):
        self.__email = email

    def set_amount(self, amount):
        self.__amount = amount

    def get_email(self):
        return self.__email

    def get_amount(self):
        return self.__amount
