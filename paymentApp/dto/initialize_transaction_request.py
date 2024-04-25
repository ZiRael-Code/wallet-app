class Initialize_transaction_request:
    def __init__(self, email, amount):
        self.email = email
        self.amount = amount

    def set_email(self, email):
        self.email = email

    def set_amount(self, amount):
        self.amount = amount

    def get_email(self):
        return self.email

    def get_amount(self):
        return self.amount
