from walletApp.dto.request.Withdraw_request import WithdrawalRequest
from walletApp.dto.request.fund_wallet_request import FundWalletRequest
from walletApp.dto.response.withdrawl_response import WithdrawResponse
from walletApp.enum.payment_status import PaymentStatus
from walletApp.models import Transaction, E_Wallet


def map_transaction(amount, description, reference, wallet_id, payment_type):
    transaction = Transaction.objects.create(amount=amount, description=description, wallet_id_id=wallet_id,
                                             reference=reference,
                                             paymentType=payment_type,
                                             paymentStatus=PaymentStatus.pending)
    return transaction


def map_withdraw_response(request: Transaction) -> WithdrawResponse:
    return WithdrawResponse(amount=request.amount,
                            description=request.description,
                            payment_type=request.paymentType, payment_status=request.paymentStatus,
                            date_created=request.date_created)


def map_fund_request(request, user) -> FundWalletRequest:
    print(user)
    return FundWalletRequest(amount=request.get('amount'), email=user.email)


def map_transfer_request(request, user) -> WithdrawalRequest:
    return WithdrawalRequest(description=request.get('description'), amount=request.get('amount'),
                             bank_name=request.get('bank_name'), account_number=request.get('account_number'),
                             wallet_pin=request.get('wallet_pin'), email=user.email)


def update_wallet_successful(data, payment_type):
    reference = data['reference']
    transaction = Transaction.objects.get(reference=reference)
    transaction.paymentStatus = PaymentStatus.successful
    transaction.save()
    amount = data['amount']
    wallet = E_Wallet.objects.get(pk=transaction.wallet_id_id)
    if payment_type == "transfer":
        wallet.balance = wallet.get_balance - amount
        wallet.save()
    else:
        wallet.balance = wallet.get_balance + amount
        wallet.save()


def update_wallet_decline(data, status_type):
    reference = data['reference']
    transaction = Transaction.objects.get(reference=reference)
    if status_type == "FAILED":
        transaction.paymentStatus = PaymentStatus.failed
        transaction.save()
    else:
        transaction.paymentStatus = PaymentStatus.reverse
        transaction.save()
