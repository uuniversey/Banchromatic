from .models import DepositProducts, DepositOptions, SavingsProducts, SavingsOptions, ExchangeRates
from rest_framework import serializers


class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'


class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        read_only_fields = ('product',)
        fields = '__all__'


class SavingsProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingsProducts
        fields = '__all__'


class SavingsOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingsOptions
        read_only_fields = ('product',)
        fields = '__all__'


class ExchangeRatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRates
        fields = '__all__'