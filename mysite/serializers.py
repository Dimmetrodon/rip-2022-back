from mysite.models import Apartments, Users, ApartmentSell
from rest_framework import serializers


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Users

        # Поля, которые мы сериализуем
        fields = ["pk", "user_name", "contact_number"]


class ApartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Apartments

        # Поля, которые мы сериализуем
        fields = ["pk", "name", "description", "owner", "cost"]


class ApartmentSellSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = ApartmentSell

        # Поля, которые мы сериализуе
        fields = ["pk", "post_date", "status", "apartment", "buyer"]
