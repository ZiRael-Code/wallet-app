from django.db import models


class PaymentStatus(models.TextChoices):
    pending = "pending"
    successful = "successful"
    failed = "failed"
    reverse = "reverse"
