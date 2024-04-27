from django.contrib import admin

from walletApp.models import E_Wallet, Transaction


# Register your models here.

@admin.register(E_Wallet)
class FastWalletEwallet(admin.ModelAdmin):
    list_display = ['balance', 'user']


@admin.register(Transaction)
class FastWalletTransactions(admin.ModelAdmin):
    list_display = ['amount', 'description', 'reference', 'paymentStatus', 'paymentType', 'date_created', 'wallet_id']
