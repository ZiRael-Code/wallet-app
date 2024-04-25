from ..dto.initialize_transaction_request import Initialize_transaction_request
from ..dto.recipient_request import RecipientRequest
from ..dto.find_bank_request import FindBankRequest
from ..dto.verify_account import VerifyAccountRequest
from ..dto.transfer_request import TransferRequest


class PaymentService:
    def initialize_transaction(self, request: Initialize_transaction_request):
        pass

    def create_transfer_recipient(self, request: RecipientRequest):
        pass

    def find_bank(self, request: FindBankRequest):
        pass

    def verify_bank_account(self, request: VerifyAccountRequest):
        pass

    def transfer(self, request: TransferRequest):
        pass

    def verify_payment(self, request):
        pass
