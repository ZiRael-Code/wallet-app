import hashlib
import hmac

import requests

from fast_wallet import settings
from .payment_service import PaymentService
from ..dto.initialize_transaction_request import Initialize_transaction_request
from ..dto.verify_account import VerifyAccountRequest
from ..dto.transfer_request import TransferRequest
from ..util.Token import TokenAuth
from ..dto.recipient_request import RecipientRequest
from ..dto.find_bank_request import FindBankRequest
from ..Exception.details_not_found_exception import InvalidDetails


class PayStackService(PaymentService):
    def __init__(self):
        self._token = TokenAuth(settings.PAYSTACK_SECRETE_KEY)

    def initialize_transaction(self, request: Initialize_transaction_request):
        url = settings.PAYSTACK_INITIALIZE_TRANSACTION_URL
        responses = requests.post(url, json={
            "email": request.get_email(),
            "amount": request.amount,
        }, auth=self._token)
        print(responses.json()["data"])
        return responses.json()["data"]

    def find_bank(self, request: FindBankRequest):
        data = requests.get(settings.PAYSTACK_FIND_BANK_URL,
                            auth=TokenAuth(settings.PAYSTACK_SECRETE_KEY))
        value = data.json()
        if value['status']:
            banks = value['data']
            bank_details = next(filter(lambda x: x['name'] == request.get_bank_name(), banks), None)
            if bank_details:
                bank_code = bank_details.get('code')
                return bank_code
            raise InvalidDetails("Bank name doesn't exist")
        else:
            return None

    def verify_bank_account(self, request: VerifyAccountRequest):
        bank_code = self.find_bank(FindBankRequest(request.get_bank_name()))
        url = f"{settings.PAYSTACK_VERIFY_ACCOUNT_BANK_URL}={request.get_account_number()}&bank_code={bank_code}"
        responses = requests.get(url, auth=self._token)
        if responses.json()['status']:
            return bank_code
        raise InvalidDetails('Invalid Bank details')

    def create_transfer_recipient(self, request: RecipientRequest):
        bank_code = self.verify_bank_account(VerifyAccountRequest(request.get_bank_name(),
                                                                  request.get_account_number()))
        payload = {
            "type": "nuban",
            "name": request.bank_name,
            "account_number": request.account_number,
            "bank_code": bank_code,
            "currency": "NGN"
        }
        responses = requests.post(settings.PAYSTACK_TRANSFER_RECIPIENT_URL,
                                  auth=self._token, json=payload)
        return responses.json()['data']['recipient_code']

    def transfer(self, request: TransferRequest):
        recipient = self.create_transfer_recipient(
            RecipientRequest(request.get_bank_name(), request.get_account_number()))
        payload = {
            "source": "balance",
            "amount": request.get_amount(),
            "reference": request.get_reference(),
            "recipient": recipient,
            "reason": request.get_description()
        }
        responses = requests.post(settings.PAYSTACK_TRANSFER_URL, auth=self._token, json=payload)
        return responses.json()['status']

    def verify_payment(self, request):
        data = request.body
        header = request.headers.get(settings.PAYSTACK_VERIFY_URL)
        expected_signature = hmac.new(settings.PAYSTACK_SECRETE_KEY.encode(), data, hashlib.sha512).hexdigest()

        if header == expected_signature:
            return data
        raise
