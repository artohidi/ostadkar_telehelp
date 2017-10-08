from django.conf.urls import url
from django.contrib import admin
from telehelp_app import views
from bot_text_list import bot_text_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^customerCategoryList/', views.CustomerCategoryViewSet.as_view(), name='customerCategory'),
    url(r'^customerQuestionList/', views.CustomerQuestionViewSet.as_view(), name='customerQuestion'),
    url(r'^providerCategoryList/', views.ProviderCategoryViewSet.as_view(), name='providerCategory'),
    url(r'^providerQuestionList/', views.ProviderQuestionViewSet.as_view(), name='providerCategory'),
    url(r'^setUserID/', views.set_user_id, name='setUserId'),
    url(r'^getUserState/', views.get_user_state, name='get_user_state'),
    url(r'^setUserState/', views.set_user_state, name='set_user_state'),
    url(r'^addQuestionAdmin/', views.add_question_admin, name='add_question_admin'),
    url(r'^userLogData/', views.user_log_data, name='user_log_data'),
    url(r'^startMenu/', views.StartMenuViewSet.as_view(), name='start_menu'),
    url(r'^userOpinion/', views.user_opinion, name='user_opinion'),
    url(r'^userAsk/', views.user_ask, name='user_ask'),
    url(r'^usersAccount/', views.UsersAccount.as_view(), name='users_account'),
    url(r'^telegramTextCategory/', bot_text_views.TelegramTextCategoryViewSet.as_view(), name='telegram_text_category'),
    url(r'^telegramText/', bot_text_views.TelegramTextViewSet.as_view(), name='telegram_text'),
    url(r'^telegramState/', bot_text_views.TelegramStateViewSet.as_view(), name='telegram_state'),
    url(r'^questionAnswer/', views.question_answer, name='question_answer'),
]
