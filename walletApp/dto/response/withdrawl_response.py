class WithdrawResponse:
    def __init__(self, amount, payment_status, payment_type, date_created, description):
        self._amount = amount
        self._payment_status = payment_status
        self._payment_type = payment_type
        self._date_created = date_created
        self._description = description

    def set_payment_status(self, payment_status):
        self._payment_status = payment_status

    def get_payment_status(self):
        return self._payment_status

    def set_payment_type(self, payment_type):
        self._payment_type = payment_type

    def set_description(self, description):
        self._description = description

    def set_date_created(self, date_created):
        self._date_created = date_created

    def get_amount(self):
        return self._amount

    def get_description(self):
        return self._description

    def get_date_created(self):
        return self._date_created

    def get_payment_type(self):
        return self._payment_type


