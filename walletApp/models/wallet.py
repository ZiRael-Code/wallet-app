from django.db import models

from fast_wallet import settings


class E_Wallet(models.Model):
    balance = models.FloatField(default=0.00)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pin = models.CharField(max_length=4, default=0000)

    def __str__(self):
        return f"{self.id}"

    @property
    def get_balance(self):
        return self.balance
