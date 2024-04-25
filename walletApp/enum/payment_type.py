from django.db import models


class PaymentType(models.TextChoices):
    deposit = "deposit"
    transfer = "transfer"
