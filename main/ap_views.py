"""
APIView uchun ishlatiladi.
"""

from rest_framework.views import APIView
from rest_framework import authentication, permissions, status
from rest_framework.response import Response

from main.models import Account
from main.serializers import AccountListSerializer, AccountPutSerializer


class AccountListAPIView(APIView):
    """
    Barcha Account listlarni qaytaradi
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        """
        list(get surovini qaytarish uchun
        :param request:
        :param format:
        :return:
        """
        accounts = Account.objects.all()
        serializer = AccountListSerializer(accounts, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        list(post qushi va bazaga kiritish uchun )
        :param request:
        :param format:
        :return:Response(serializer.data, status=status.HTTP_200_OK)
        """
        serializer = AccountListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountDetailAPView(APIView):
    """
    Retrieve,update or delete a account modelni oladi.
    """

    def get_object(self, guid):
        """

        :param guid:
        :return:
        """
        try:
            return Account.objects.get(guid=guid)
        except Account.DoesNotExist:
            pass

    def get(self, request, guid, format=None):
        account = self.get_object(guid)
        serializer = AccountListSerializer(account)
        return Response(serializer.data)

    def put(self, request, guid, format=None):
        account = self.get_object(guid)
        serializer = AccountPutSerializer (account,  data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, guid, format=None):
        account = self.get_object(guid)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
