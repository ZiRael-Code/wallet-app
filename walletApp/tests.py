from user.models import User
from walletApp.dto.request.Withdraw_request import WithdrawalRequest
from walletApp.dto.request.fund_wallet_request import FundWalletRequest
from walletApp.exception.wallet_exception import WalletNotExistException
from walletApp.models.wallet import E_Wallet
from rest_framework.test import APITestCase

from walletApp.services.walletApp_service import WalletAppServiceImpl
from walletApp.services.wallet_service import WalletAppService


# Create your tests here.


class TestWallet(APITestCase):
    def setUp(self):
        user = User.objects.create(email="ope@gmail.com", username="shola", password="12345")
        wallets = E_Wallet.objects.create(pin="1234", user_id=user.pk)

    def test_fundWallet(self):
        wallet: WalletAppService = WalletAppServiceImpl()
        result = wallet.fund_wallet(FundWalletRequest(amount=200.00, email="ope@gmail.com"))
        self.assertIsNotNone(result)

    def test_withdrawal(self):
        wallet: WalletAppService = WalletAppServiceImpl()
        result = wallet.fund_wallet(FundWalletRequest(amount=400.00, email="ope@gmail.com"))
        result = wallet.withdraw(WithdrawalRequest(amount=200, description="water plumbing",
                                                   bank_name="Ecobank Nigeria", account_number=1381014377,
                                                   wallet_pin="1234", email="ope@gmail.com"))
        self.assertEquals(200, wallet.get_wallet("ope@gmail.com").balance)

    def test_get_balance(self):
        wallet: WalletAppService = WalletAppServiceImpl()
        balance = wallet.get_balance("ope@gmail.com")
        self.assertEquals(0.00, balance)

    def test_get_balance_if_user_doesnt_exist(self):
        wallet: WalletAppService = WalletAppServiceImpl()
        self.assertRaises(WalletNotExistException, lambda: wallet.get_balance("ope2@gmail.com"))

    def test_transaction_history(self):
        wallet: WalletAppService = WalletAppServiceImpl()
        transaction_history = wallet.get_all_transaction("ope@gmail.com")
        self.assertEquals(0, len(transaction_history))
