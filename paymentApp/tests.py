from rest_framework.test import APITestCase
from .dto.find_bank_request import FindBankRequest
from .dto.initialize_transaction_request import Initialize_transaction_request
from .dto.recipient_request import RecipientRequest
from .dto.transfer_request import TransferRequest
from .dto.verify_account import VerifyAccountRequest
from .service.payment_service import PaymentService
from .service.paystack_service import PayStackService
from .Exception.details_not_found_exception import InvalidDetails
from walletApp.util.generate_unique_id import generate_unique_id


# Create your tests here.

class TestPaymentService(APITestCase):
    def test_find_bank(self):
        account_number = FindBankRequest("Kuda Bank")
        payment_service: PaymentService = PayStackService()
        bank_details = payment_service.find_bank(account_number)
        self.assertEqual('50211', bank_details)

    def test_bank_Doesnt_exist(self):
        account_number = FindBankRequest("Kudas Bank")
        payment_service: PaymentService = PayStackService()
        self.assertRaises(InvalidDetails, lambda: payment_service.find_bank(account_number))

    def test_verify_bank_account_details(self):
        account_details = VerifyAccountRequest("Ecobank Nigeria", 1381014377)
        payment_service: PaymentService = PayStackService()
        value = payment_service.verify_bank_account(account_details)
        self.assertEquals('050', value)

    def test_create_transfer_recipient(self):
        account_details = RecipientRequest("Ecobank Nigeria", 1381014377)
        payment_service: PaymentService = PayStackService()
        result = payment_service.create_transfer_recipient(account_details)
        self.assertIsNotNone(result)

    def test_transfer(self):
        ids = generate_unique_id()
        account_details = TransferRequest(amount=100, description="my sister feeding", account_number=1381014377,
                                          bank_name="Ecobank Nigeria", reference=ids)
        payment_service: PaymentService = PayStackService()
        result = payment_service.transfer(account_details)
        self.assertTrue(result)

    def test_initialize_transaction(self):
        payment_service:PaymentService = PayStackService()
        response = payment_service.initialize_transaction(Initialize_transaction_request(amount=200.00,
                                                                                         email="ope@gmail.com"))
        print(response)
        self.assertIsNotNone(response)