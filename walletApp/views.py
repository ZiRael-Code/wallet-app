from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from fast_wallet import settings

from walletApp.services.walletApp_service import WalletAppServiceImpl
from walletApp.services.wallet_service import WalletAppService
from .exception.amount_exception import AmountException
from .exception.insufficient_funds import InsufficientFundsException
from .exception.invalid_pin import InvalidPinException
from .exception.wallet_exception import WalletNotExistException
from .models import Transaction
from .util.mapper import map_fund_request, map_transfer_request
from .serializer import TransactionSerializer

# Create your views here.
payment: WalletAppService = WalletAppServiceImpl()


class VerifyPayment(APIView):
    def post(self, request):
        print(request)
        response = payment.verify_payment(request)
        return Response(response.get_message(), status=status.HTTP_200_OK)


class FundWallet(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            response = payment.fund_wallet(map_fund_request(request.data, request.user))
            return Response({"message":response.get_message()}, status=status.HTTP_200_OK)
        except AmountException as exception:
            return Response({"Message": exception.get_message()}, status=status.HTTP_400_BAD_REQUEST)
        except WalletNotExistException as exception:
            return Response({"Message": exception.get_message()}, status=status.HTTP_400_BAD_REQUEST)


class Withdraw(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            response = payment.withdraw(map_transfer_request(request.data, request.user))
            serializer = TransactionSerializer(response)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except InsufficientFundsException as exception:
            return Response({'message': exception.get_message()}, status=status.HTTP_400_BAD_REQUEST)
        except WalletNotExistException as exception:
            return Response({'message': exception.get_message()}, status=status.HTTP_400_BAD_REQUEST)
        except InvalidPinException as exception:
            return Response({'message': exception.get_message()}, status=status.HTTP_400_BAD_REQUEST)


class Transactions(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = payment.get_all_transaction(request.user)
        serializer = TransactionSerializer(response, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetBalance(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            response = payment.get_balance(request.user)
            return Response({"balance": response}, status=status.HTTP_200_OK)
        except WalletNotExistException as exception:
            return Response({"Message:", exception.get_message()}, status=status.HTTP_400_BAD_REQUEST)
