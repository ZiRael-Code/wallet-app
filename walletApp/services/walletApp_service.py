from rest_framework import status
from rest_framework.utils import json

from paymentApp.dto.initialize_transaction_request import Initialize_transaction_request
from paymentApp.dto.transfer_request import TransferRequest
from paymentApp.service.payment_service import PaymentService
from paymentApp.service.paystack_service import PayStackService
from walletApp.dto.request.Withdraw_request import WithdrawalRequest
from walletApp.dto.request.fund_wallet_request import FundWalletRequest
from walletApp.dto.response.fund_wallet_response import FundWalletResponse
from walletApp.dto.response.webhook_response import WebhookResponse
from walletApp.dto.response.withdrawl_response import WithdrawResponse
from walletApp.enum.payment_status import PaymentStatus
from walletApp.enum.payment_type import PaymentType
from walletApp.exception.amount_exception import AmountException
from walletApp.exception.wallet_exception import WalletNotExistException
from walletApp.models import Transaction, E_Wallet
from walletApp.services.wallet_service import WalletAppService
from walletApp.util.generate_unique_id import generate_unique_id
from walletApp.util.mapper import map_transaction, map_withdraw_response, update_wallet_successful, \
    update_wallet_decline


class WalletAppServiceImpl(WalletAppService):
    def __init__(self):
        self._payment_service: PaymentService = PayStackService()

    def fund_wallet(self, request: FundWalletRequest):
        if request.get_amount() < 5:
            raise AmountException("amount too low")
        amount_in_naira = request.get_amount() * 100
        wallet = self.get_wallet(request.get_email())
        response = self._payment_service.initialize_transaction(
            Initialize_transaction_request(email=request.get_email(),
                                           amount=amount_in_naira))
        map_transaction(amount=request.get_amount(), description="Deposit", reference=response['reference'],
                        wallet_id=wallet.id, payment_type=PaymentType.deposit)
        return FundWalletResponse(response["authorization_url"])

    def withdraw(self, request: WithdrawalRequest):
        generate_reference = generate_unique_id()
        wallet = self.get_wallet(request.get_email())
        transaction = map_transaction(amount=request.get_amount(), description=request.get_description(),
                                      reference=generate_reference, wallet_id=wallet.id,
                                      payment_type=PaymentType.transfer)
        transfers = self._payment_service.transfer(TransferRequest(amount=request.get_amount(),
                                                                   description=request.get_description(),
                                                                   bank_name=request.get_bank_name(),
                                                                   account_number=request.get_account_number(),
                                                                   reference=generate_reference))
        return transaction

    def verify_payment(self,request):
        data = self._payment_service.verify_payment(request)
        data = json.loads(data)
        event = data['event']
        datas = data['data']
        print(data)
        if event == 'charge.success':
            update_wallet_successful(datas, PaymentType.deposit)
        if event == 'transfer.success':
            update_wallet_successful(datas, PaymentType.transfer)
        if event == 'transfer.failed':
            update_wallet_decline(datas, PaymentStatus.failed)
        if event == 'transfer.reversed':
            update_wallet_decline(datas, PaymentStatus.reverse)
        return WebhookResponse("Successful")

    def get_balance(self, request):
        wallet = self.get_wallet(request.email)
        return wallet.get_balance

    def get_wallet(self, email):
        wallet = next(filter(lambda x: x.user.email == email, E_Wallet.objects.all()), None)
        if wallet is None:
            raise WalletNotExistException("Wallet doesn't exist")
        return wallet

    def get_all_transaction(self, user):
        wallet = self.get_wallet(user.email)
        transactions = Transaction.objects.filter(wallet_id_id=wallet)
        return transactions
