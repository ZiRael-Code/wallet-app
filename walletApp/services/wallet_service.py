from walletApp.dto.request.Withdraw_request import WithdrawalRequest
from walletApp.dto.request.fund_wallet_request import FundWalletRequest


class WalletAppService:
    def fund_wallet(self, request: FundWalletRequest):
        pass

    def withdraw(self, request: WithdrawalRequest):
        pass

    def verify_payment(self, request):
        pass

    def get_balance(self, request):
        pass

    def get_wallet(self, email):
        pass

    def get_all_transaction(self, user):
        pass
