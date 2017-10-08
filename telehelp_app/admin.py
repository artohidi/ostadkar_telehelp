from django.contrib import admin
from .models import CustomerCategory, CustomerQuestions, ProviderCategory, ProviderQuestions, StartMenu, \
    UserInformation, UsersLog, UsersOpinion, UsersAsk


def make_activate(modeladmin, request, queryset):
    queryset.update(status='فعال')


def make_deactivate(modeladmin, request, queryset):
    queryset.update(status='غیرفعال')


def home_page_set(modeladmin, request, queryset):
    queryset.update(state='صفحه اصلی')


def answered(modeladmin, request, queryset):
    queryset.update(ask_state='پاسخ داده‌شده')


def not_answered(modeladmin, request, queryset):
    queryset.update(ask_state='پاسخ داده‌نشده')


def seen(modeladmin, request, queryset):
    queryset.update(opinion_state='دیده شده')


def not_seen(modeladmin, request, queryset):
    queryset.update(opinion_state='دیده نشده')


def accepted(modeladmin, request, queryset):
    queryset.update(opinion_state='قبول شده')


def ignored(modeladmin, request, queryset):
    queryset.update(opinion_state='رد شده')


def done(modeladmin, request, queryset):
    queryset.update(opinion_state='انجام شده')


make_activate.short_description = "فعال کردن کاربرهای انتخابی"
make_deactivate.short_description = "غیرفعال کردن کاربرهای انتخابی"
answered.short_description = "وضعیت پاسخ‌داده‌شده به موارد انتخابی"
not_answered.short_description = "وضعیت پاسخ‌داده‌نشده به موارد انتخابی"
home_page_set.short_description = "ریست کردن موقعیت موارد انتخابی"
seen.short_description = "وضعیت دیده‌شده به موارد انتخابی"
not_seen.short_description = "وضعیت دیده‌ نشده به موارد انتخابی"
accepted.short_description = "وضعیت قبول شده به موارد انتخابی"
ignored.short_description = "وضعیت رد شده به موارد انتخابی"
done.short_description = "وضعیت انجام‌ شده به موارد انتخابی"


class UsersAskAdmin(admin.ModelAdmin):
    readonly_fields = ['id', 'user_id', 'first_name', 'last_name', 'username', 'ask_text', 'ask_time', ]
    list_display = (
        "id", "user_id", "username", "first_name", "last_name", "ask_time", "ask_category", "ask_text", "answer_button")
    ordering = ('-ask_time', 'ask_state',)
    list_filter = ('ask_state', 'ask_category')
    actions = [answered, not_answered]

    def answer_button(self, obj):
        return u'<form action="http://127.0.0.1:8000/questionAnswer/"><input type="text" name="answer">' \
               u'<br><button type="submit">send</button><br></form>'

    answer_button.allow_tags = True
    answer_button.short_description = "پاسخ دادن"


class UsersOpinionAdmin(admin.ModelAdmin):
    readonly_fields = ['id', 'user_opinion_id', 'first_name', 'last_name', 'username', 'user_opinion_time',
                       'user_opinion_text']
    list_display = (
        "user_opinion_id", "username", "first_name", "last_name", "user_opinion_text", "user_opinion_time",
        "opinion_state_colored")
    ordering = ('-user_opinion_time', 'opinion_state',)
    list_filter = ('opinion_state',)
    actions = [seen, not_seen, accepted, ignored, done]

    def opinion_state_colored(self, obj):
        if obj.opinion_state == 'دیده شده':
            return u'<h3 style="color:#3380cc;">{0}</h3>'.format(obj.opinion_state)
        elif obj.opinion_state == 'انجام شده':
            return u'<h3 style="color:#33cc33;">{0}</h3>'.format(obj.opinion_state)
        elif obj.opinion_state == 'دیده نشده':
            return u'<h3 style="color:#cc3333;">{0}</h3>'.format(obj.opinion_state)
        else:
            return obj.opinion_state

    opinion_state_colored.allow_tags = True
    opinion_state_colored.short_description = 'وضعیت پیشنهاد'


class StartMenuAdmin(admin.ModelAdmin):
    list_display = ("menu_name", "category_priority", "changedTime", "createdTime")
    ordering = ('category_priority',)
    list_display_links = ('menu_name', 'category_priority',)


class CustomerCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['menu_name']
    list_display = ("id", "category_name", "category_description", "category_priority", "changedTime", "createdTime")
    ordering = ('category_priority',)
    list_display_links = ('category_name', 'category_priority',)


class CustomerQuestionsAdmin(admin.ModelAdmin):
    list_display = (
        "category_name", "question_priority", "question_name", "question_answer", "changedTime", "createdTime")
    ordering = ('category_name', 'question_priority',)
    list_display_links = ('category_name', 'question_priority',)
    list_filter = ('category_name',)


class ProviderCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['menu_name']
    list_display = ("category_name", "category_description", "category_priority", "changedTime", "createdTime")
    ordering = ('category_priority',)
    list_display_links = ('category_name', 'category_priority',)


class ProviderQuestionsAdmin(admin.ModelAdmin):
    list_display = (
        "category_name", "question_priority", "question_name", "question_answer", "changedTime", "createdTime")
    ordering = ('category_name', 'question_priority',)
    list_display_links = ('category_name', 'question_priority',)
    list_filter = ('category_name',)


class UserInformationAdmin(admin.ModelAdmin):
    list_display = ("user_id_colored", "changed_username", "changed_first_name", "changed_last_name", "status_colored",
                    "state", "createdUserTime", "changedUserTime")
    readonly_fields = ["user_id", "changed_username", "changed_first_name", "changed_last_name", "createdUserTime",
                       "changedUserTime"]
    ordering = ('-changedUserTime',)
    list_display_links = ('user_id_colored', 'changed_username', 'changed_first_name', 'changed_last_name',
                          'status_colored')
    list_filter = ('status', 'state', 'account_type',)
    actions = [make_activate, make_deactivate, home_page_set]

    def status_colored(self, obj):
        if obj.status != 'غیرفعال':
            return u'<h3 style="color:#33cc33;">{0}</h3>'.format(obj.status)
        else:
            return u'<h3 style="color:#cc3333;">{0}</h3>'.format(obj.status)

    def user_id_colored(self, obj):
        if obj.status != 'غیرفعال':
            return u'<h3 style="color:#33cc33;">{0}</h3>'.format(obj.user_id)
        else:
            return u'<h3 style="color:#cc3333;">{0}</h3>'.format(obj.user_id)

    def changed_username(self, obj):
        if obj.username == '':
            obj.username = 'ندارد'
        return obj.username

    def changed_first_name(self, obj):
        if obj.first_name == '':
            obj.first_name = 'ندارد'
        return obj.first_name

    def changed_last_name(self, obj):
        if obj.last_name == '':
            obj.last_name = 'ندارد'
        return obj.last_name

    status_colored.allow_tags = True
    status_colored.short_description = 'وضعیت کاربر'
    user_id_colored.allow_tags = True
    user_id_colored.short_description = 'وضعیت کاربر'
    changed_username.allow_tags = True
    changed_username.short_description = 'نام کاربری انخابی'
    changed_first_name.allow_tags = True
    changed_first_name.short_description = 'نام کاربر'
    changed_last_name.allow_tags = True
    changed_last_name.short_description = 'فامیلی کاربر'


admin.site.register(UsersOpinion, UsersOpinionAdmin)
admin.site.register(UsersLog)
admin.site.register(StartMenu, StartMenuAdmin),
admin.site.register(CustomerCategory, CustomerCategoryAdmin),
admin.site.register(CustomerQuestions, CustomerQuestionsAdmin),
admin.site.register(ProviderCategory, ProviderCategoryAdmin),
admin.site.register(ProviderQuestions, ProviderQuestionsAdmin),
admin.site.register(UserInformation, UserInformationAdmin),
admin.site.register(UsersAsk, UsersAskAdmin)
