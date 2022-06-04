from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets, permissions, generics, mixins

from .models import Account, Transaction

# Serializers define the API representation.

class TransactionsSerializer(serializers.ModelSerializer):
    # customerID = BalanceSerializer(many=False, read_only=True)

    class Meta:
        model = Transaction
        fields = ['amount']


class TransactionListingField(serializers.RelatedField):
    def to_representation(self, value):
        return 'Date: %s, Quantity: %d' % (value.date, value.amount)


class BalanceSerializer(serializers.ModelSerializer):
    transactions = TransactionListingField(many=True,
                                            read_only=True)
    first_name = serializers.CharField(source="customerID.first_name")
    last_name  = serializers.CharField(source="customerID.last_name")
    
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'balance', 'transactions']
       


# class UserSerializer(serializers.ModelSerializer):
#     # balance = BalanceSerializer(many=True)
#     customer = serializers.SlugRelatedField(slug_field='balance',
#                                             many=False,
#                                             read_only=True)

#     class Meta:
#         model = User
#         # fields = ['url', 'username', 'email', 'is_staff']
#         fields = ['id', 'first_name', 'last_name', 'customer']


# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer



class BalanceViewSet(mixins.ListModelMixin,
                     viewsets.GenericViewSet):#generics.ListAPIView):#ModelViewSet):
    # queryset = Account.objects.all()
    serializer_class = BalanceSerializer

    def get_queryset(self):
        queryset = Account.objects.all()
        userID = self.request.query_params.get('customer')
        if userID is not None:
            queryset = queryset.filter(customerID__id=userID)
        return queryset


class TransactionsViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionsSerializer

