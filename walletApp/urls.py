from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter

from .views import Transactions

urlpatterns = [
    path('webhook', views.VerifyPayment.as_view(), name='verify_payment'),
    path('funds/', views.FundWallet.as_view(), name='fund_wallet'),
    path('transfer/', views.Withdraw.as_view(), name="transfer"),
    path("transaction/", views.Transactions.as_view(), name="all_transaction"),
    path("balance/", views.GetBalance.as_view(), name="balance"),
]
