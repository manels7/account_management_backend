from rest_framework import routers, serializers, viewsets, mixins

from .models import Account, Transaction


# Serializers

class TransactionListingField(serializers.RelatedField):
    def to_representation(self, value):
        return 'Date: %s, Quantity: %d' % (value.date, value.amount)

class AccountRetrieveSerializer(serializers.ModelSerializer):
    transactions = TransactionListingField(many=True, read_only=True)
    first_name = serializers.CharField(source="customerID.first_name", read_only=True)
    last_name  = serializers.CharField(source="customerID.last_name", read_only=True)
    
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'balance', 'transactions']

class AccountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['customerID', 'balance']


# API views

class AccountRetrieveViewSet(mixins.RetrieveModelMixin,
                             viewsets.GenericViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountRetrieveSerializer
    lookup_field = "customerID"


class AccountCreateViewSet(mixins.CreateModelMixin,
                          viewsets.GenericViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountCreateSerializer
      