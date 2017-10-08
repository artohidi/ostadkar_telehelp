from __future__ import unicode_literals
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from .models import CustomerCategory, CustomerQuestions, ProviderCategory, ProviderQuestions, StartMenu, \
    UserInformation, UsersLog, UsersOpinion, UsersAsk
from .serializer import CustomerCategorySerializer, CustomerQuestionSerializer, ProviderCategorySerializer, \
    ProviderQuestionSerializer, StartMenuSerializer, UsersAccountSerializer
from rest_framework.permissions import AllowAny
from django.http import JsonResponse


class StartMenuViewSet(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = StartMenuSerializer

    def get_queryset(self):
        queryset = StartMenu.objects.all()
        return queryset.order_by('category_priority')


class CustomerCategoryViewSet(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CustomerCategorySerializer

    def get_queryset(self):
        queryset = CustomerCategory.objects.all()
        return queryset.order_by('category_priority')


class CustomerQuestionViewSet(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = CustomerQuestionSerializer

    def get_queryset(self):
        queryset = CustomerQuestions.objects.all()
        return queryset.order_by('question_priority')


class ProviderCategoryViewSet(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProviderCategorySerializer

    def get_queryset(self):
        queryset = ProviderCategory.objects.all()
        return queryset.order_by('category_priority')


class ProviderQuestionViewSet(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ProviderQuestionSerializer

    def get_queryset(self):
        queryset = ProviderQuestions.objects.all()
        return queryset.order_by('question_priority')


@csrf_exempt
def set_user_id(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id_get = data.get("user_id", "")
        username_get = data.get("username", "")
        first_name_get = data.get("first_name", "")
        last_name_get = data.get("last_name", "")
        user_get = UserInformation.objects.filter(user_id=user_id_get).first()
        if user_get is None:
            user = UserInformation.objects.create(user_id=user_id_get, username=username_get, first_name=first_name_get,
                                                  last_name=last_name_get)
            user.save()
            return JsonResponse({"user": "جدید", "status": "فعال"})
        else:
            return JsonResponse({"user": "وجوددارد", "status": user_get.status})


@csrf_exempt
def get_user_state(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id_get = data.get("user_id", "")
        user_get = UserInformation.objects.filter(user_id=user_id_get).first()
        if user_get is None:
            return JsonResponse({"user": "وجودندارد"})
        else:
            return JsonResponse({"user": "وجوددارد", "state": user_get.state, "status": user_get.status,
                                 "account_type": user_get.account_type})


@csrf_exempt
def set_user_state(request):
    if request.method == 'POST':
        param = json.loads(request.body)
        user_id_get = param.get("user_id", "")
        user_state_get = param.get("state", "")
        user_get = UserInformation.objects.filter(user_id=user_id_get).first()
        user_status_get = param.get("status", "")
        if user_status_get == 'فعال' or user_state_get == 'غیرفعال':
            user_get.state = user_state_get
            user_get.status = user_status_get
            user_get.save()
            return JsonResponse({user_get.user_id: "state and state changed"})
        else:
            user_get.state = user_state_get
            user_get.save()
            return JsonResponse({user_get.user_id: "state changed"})


@csrf_exempt
def user_log_data(request):
    if request.method == 'POST':
        param = json.loads(request.body)
        user_id_get = param.get('user_id', '')
        user_log_data_get = param.get('user_log_data', '')
        user_log_time_get = param.get('user_log_time', '')
        user_log_message_id_get = param.get('user_log_message_id', '')
        if user_id_get != '' and user_log_data_get != '':
            log = UsersLog.objects.create(user_id=user_id_get, user_log_data=user_log_data_get,
                                          user_log_time=user_log_time_get, user_log_message_id=user_log_message_id_get)
            log.save()
            return JsonResponse({"log": "saved"})
        else:
            return JsonResponse({"log": "not saved"})


@csrf_exempt
def user_opinion(request):
    if request.method == 'POST':
        param = json.loads(request.body)
        user_opinion_id_get = param.get('user_opinion_id', '')
        user_opinion_text_get = param.get('user_opinion_text', '')
        username_get = param.get('username', '')
        first_name_get = param.get('first_name', '')
        last_name_get = param.get('last_name', '')
        opinion = UsersOpinion.objects.create(user_opinion_id=user_opinion_id_get,
                                              user_opinion_text=user_opinion_text_get, username=username_get,
                                              first_name=first_name_get, last_name=last_name_get)
        opinion.save()
        return JsonResponse({"opinion": "saved"})
    else:
        return JsonResponse({"opinion": "not saved"})


@csrf_exempt
def user_ask(request):
    if request.method == 'POST':
        param = json.loads(request.body)
        user_id_get = param.get('user_id', '')
        ask_text_get = param.get('ask_text', '')
        username_get = param.get('username', '')
        first_name_get = param.get('first_name', '')
        last_name_get = param.get('last_name', '')
        ask_category_get = param.get('ask_category', '')
        ask = UsersAsk.objects.create(user_id=user_id_get,
                                      ask_text=ask_text_get, username=username_get,
                                      first_name=first_name_get, last_name=last_name_get, ask_category=ask_category_get)
        ask.save()
        return JsonResponse({"ask": "saved"})
    else:
        return JsonResponse({"ask": "not saved"})


class UsersAccount(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UsersAccountSerializer

    def get_queryset(self):
        queryset = UserInformation.objects.all()
        return queryset


@csrf_exempt
def add_question_admin(request):
    if request.method == 'POST':
        param = json.loads(request.body)
        question_type_get = param.get('question_type', '')
        category_name_get = param.get('category_name', '')
        question_name_get = param.get('question_name', '')
        question_answer_get = param.get('question_answer', '')
        question_priority_get = param.get('question_priority', '')
        if question_type_get == "مشتری":
            question_set = CustomerQuestions.objects.create(
                category_name=CustomerCategory.objects.get(id=category_name_get),
                question_name=question_name_get,
                question_answer=question_answer_get,
                question_priority=question_priority_get)
            question_set.save()
            return JsonResponse({"question": "saved"})
        elif question_type_get == "سرویس دهنده":
            question_set = ProviderQuestions.objects.create(
                category_name=ProviderCategory.objects.get(id=category_name_get),
                question_name=question_name_get,
                question_answer=question_answer_get,
                question_priority=question_priority_get)
            question_set.save()
            return JsonResponse({"question": "saved"})
        else:
            return JsonResponse({"question": "not saved"})


@csrf_exempt
def question_answer(request):
    if request.method == 'GET':
        input(request)
