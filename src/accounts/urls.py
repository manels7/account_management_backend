from .api import AccountRetrieveViewSet, AccountCreateViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'retrieve', AccountRetrieveViewSet, basename='Account')
router.register(r'create', AccountCreateViewSet, basename='Account')

