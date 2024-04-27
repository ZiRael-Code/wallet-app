from django.contrib.auth.admin import UserAdmin
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from walletApp.models.wallet import E_Wallet

from user.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, max_length=16, write_only=True)
    wallet_pin = serializers.CharField(min_length=4, max_length=4, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'wallet_pin']

    def create(self, validated_data):
        pin = validated_data.get('wallet_pin')
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = User.objects.create_user(username=username, email=email, password=password)
        E_Wallet.objects.create(user_id=user.pk, pin=pin)
        return user
