from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets, permissions

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class BalanceView():
    # permission_classes = [permissions.IsAuthenticated]
    pass


class TransactionsView():
    # permission_classes = [permissions.IsAuthenticated]
    pass



