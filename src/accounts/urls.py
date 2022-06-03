from .api import UserViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)