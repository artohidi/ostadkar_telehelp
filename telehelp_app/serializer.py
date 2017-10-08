from rest_framework import serializers
from .models import CustomerCategory, CustomerQuestions, UserInformation


class StartMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerCategory
        fields = 'menu_name', 'category_priority',


class CustomerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerCategory
        fields = 'id', 'category_name', 'category_description', 'category_priority'


class CustomerQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerQuestions
        fields = 'category_name', 'question_name', 'question_answer', 'question_priority'


class ProviderCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerCategory
        fields = 'id', 'category_name', 'category_description', 'category_priority'


class ProviderQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerQuestions
        fields = 'category_name', 'question_name', 'question_answer', 'question_priority'


class GetUpdateDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformation
        fields = '__all__'


class UsersAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformation
        fields = '__all__'
