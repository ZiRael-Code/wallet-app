from django.contrib.auth import authenticate
from rest_framework.utils import json

from .user_services import UserService
from ..exception.Invalid_details import InvalidDetailsException
from ..serializer import RegisterSerializer
from ..models import User
from ..util.token import get_tokens_for_user
from walletApp.models.wallet import E_Wallet


class UserServiceImp(UserService):
    def __init__(self):
        self._serializer = RegisterSerializer

    def register(self, request):
        serializer = self._serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data

    def login(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            get_user = User.objects.get(username=username)
            token = get_tokens_for_user(get_user)
            return token
        else:
            raise  InvalidDetailsException("Invalid credential")
