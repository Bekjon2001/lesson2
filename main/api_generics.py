"""
Generics uchun ishlatiladi
"""

from rest_framework import generics
from .models import Account
from main.serializers import   AccountListSerializer, AccountCreateSerializer

# CREATE: Post
class AccountListCreateAPIView(generics.CreateAPIView):
    """
    Create a new Account.
    """
    queryset = Account.objects.all()
    serializer_class = AccountCreateSerializer


# LIST: GET
class AccountGenericListAPIView(generics.ListAPIView):
    """
    List all Accounts.
    """
    queryset = Account.objects.all()
    serializer_class = AccountListSerializer


# RETRIEVE: GET
class AccountRetrieveAPIView(generics.RetrieveAPIView):
    """
    Retrieve a single Account by GUID.
    """
    lookup_field = 'guid'
    queryset = Account.objects.all()
    serializer_class = AccountListSerializer


# UPDATE: PUT/PATCH
class AccountUpdateAPIView(generics.UpdateAPIView):
    """
    Update a single Account by GUID.
    """
    lookup_field = 'guid'
    queryset = Account.objects.all()
    serializer_class = AccountCreateSerializer


# DESTROY: DELETE
class AccountDestroyAPIView(generics.DestroyAPIView):
    """
    Delete a single Account by GUID.
    """
    lookup_field = 'guid'
    queryset = Account.objects.all()
    serializer_class = AccountListSerializer


# RETRIEVE, UPDATE, DESTROY: GET, PUT/PATCH, DELETE
class AccountRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update or Delete an Account by GUID.
    """
    lookup_field = 'guid'
    queryset = Account.objects.all()
    serializer_class = AccountListSerializer