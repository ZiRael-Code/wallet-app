from django.db import models

from .wallet import E_Wallet
from ..enum.payment_status import PaymentStatus
from ..enum.payment_type import PaymentType


class Transaction(models.Model):
    amount = models.BigIntegerField()
    description = models.CharField(max_length=255)
    wallet_id = models.ForeignKey(E_Wallet, on_delete=models.CASCADE)
    reference = models.CharField(max_length=255)
    paymentStatus = models.CharField(choices=PaymentStatus.choices, default=PaymentStatus.pending)
    paymentType = models.CharField(choices=PaymentType.choices, default=None)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.reference)
