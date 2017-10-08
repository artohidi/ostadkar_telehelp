from rest_framework import serializers
from .models import TelegramTextCategory, TelegramText, TelegramState


class TelegramTextCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramTextCategory
        fields = 'id', 'category_get',


class TelegramTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramText
        fields = 'category_get', 'text_get',


class TelegramStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramState
        fields = '__all__'
