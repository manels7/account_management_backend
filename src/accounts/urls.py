from .api import BalanceViewSet, TransactionsViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'accounts', BalanceViewSet, basename='Account')
router.register(r'transactions', TransactionsViewSet)

