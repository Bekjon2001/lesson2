from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from main.models import Account


class AccountListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"


class AccountCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"

    def create(self, validated_data):
        validated_data["password"]= make_password(validated_data["password"])
        return super(AccountCreateSerializer,self).create(validated_data)

class AccountPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'guid',
            'first_name',
            'last_name',
            'middle_name'
        ]
