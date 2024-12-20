"""
Viewset uchun ishladid
"""

from rest_framework import viewsets

from main.models import Account
from main.serializers import AccountListSerializer


class AccountViewSetsListAPIView(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountListSerializer
