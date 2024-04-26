from django.contrib.auth.admin import UserAdmin
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from walletApp.models.wallet import E_Wallet

from user.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=8, max_length=16, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        pin = validated_data.g
        user = User.objects.create_user(**validated_data)
        E_Wallet.objects.create(user_id=user.pk)
        return user
