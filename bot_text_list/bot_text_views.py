from __future__ import unicode_literals
from rest_framework import generics
from rest_framework.permissions import AllowAny
from bot_text_list.bot_text_list_serializer import TelegramTextCategorySerializer, TelegramTextSerializer, \
    TelegramStateSerializer
from .models import TelegramTextCategory, TelegramText, TelegramState


class TelegramTextCategoryViewSet(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = TelegramTextCategorySerializer

    def get_queryset(self):
        queryset = TelegramTextCategory.objects.all()
        return queryset


class TelegramTextViewSet(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = TelegramTextSerializer

    def get_queryset(self):
        queryset = TelegramText.objects.all()
        return queryset


class TelegramStateViewSet(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = TelegramStateSerializer

    def get_queryset(self):
        queryset = TelegramState.objects.all()
        return queryset
