from rest_framework import serializers

from .models.transaction import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['amount', 'description', 'reference', 'paymentStatus', 'paymentType', 'date_created']
