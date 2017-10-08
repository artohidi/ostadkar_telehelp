from django.db import models
from future.utils import python_2_unicode_compatible

choice_list = (
    ('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'),
    ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'),
    ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'),
    ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'))


@python_2_unicode_compatible
class StartMenu(models.Model):
    class Meta:
        verbose_name = "صفحه اصلی"
        verbose_name_plural = "صفحه اصلی"

    menu_name = models.CharField(max_length=200, null=False, blank=False, verbose_name="منو")
    category_priority = models.CharField(max_length=100, verbose_name="اولویت",
                                         choices=choice_list)
    createdTime = models.DateTimeField(auto_now_add=True, verbose_name="زمان ایجاد")
    changedTime = models.DateTimeField(auto_now=True, verbose_name="آخرین تغییر")

    def __str__(self):
        return str(self.menu_name)


@python_2_unicode_compatible
class CustomerCategory(models.Model):
    class Meta:
        verbose_name = "دسته بندی موضوعی مشتریان"
        verbose_name_plural = "دسته بندی موضوعی مشتریان"

    menu_name = models.CharField(max_length=200, default='سوالات مشتری', verbose_name='بخش')
    category_name = models.CharField(max_length=200, null=False, blank=False, verbose_name="نام دسته")
    category_description = models.CharField(max_length=2000, default="بدون توضیح", verbose_name="توضیحات")
    category_priority = models.CharField(max_length=100, verbose_name="اولویت",
                                         choices=choice_list)
    createdTime = models.DateTimeField(auto_now_add=True, verbose_name="زمان ایجاد")
    changedTime = models.DateTimeField(auto_now=True, verbose_name="آخرین تغییر")

    def __str__(self):
        return "{0}".format(self.category_name)


@python_2_unicode_compatible
class CustomerQuestions(models.Model):
    class Meta:
        verbose_name = "سوالات مشتریان"
        verbose_name_plural = "سوالات مشتریان"

    category_name = models.ForeignKey(CustomerCategory, on_delete=models.CASCADE, verbose_name="انتخاب دسته")
    question_name = models.CharField(max_length=200, null=False, blank=False, verbose_name="عنوان سوال")
    question_answer = models.CharField(max_length=2000, verbose_name="پاسخ سوال")
    question_priority = models.CharField(max_length=100, verbose_name="اولویت",
                                         choices=choice_list)
    createdTime = models.DateTimeField(auto_now_add=True, verbose_name="زمان ایجاد")
    changedTime = models.DateTimeField(auto_now=True, verbose_name="زمان تغییر")

    def __str__(self):
        return "{0}_{1}".format(self.question_priority, self.question_name)


@python_2_unicode_compatible
class ProviderCategory(models.Model):
    class Meta:
        verbose_name = "دسته بندی موضوعی سرویس دهندگان"
        verbose_name_plural = "دسته بندی موضوعی سرویس دهندگان"

    menu_name = models.CharField(max_length=200, default='سوالات سرویس دهنده', verbose_name='بخش')
    category_name = models.CharField(max_length=200, null=False, blank=False, verbose_name="نام دسته")
    category_description = models.CharField(max_length=2000, default="بدون توضیح", verbose_name="توضیحات")
    category_priority = models.CharField(max_length=100, verbose_name="اولویت",
                                         choices=choice_list)
    createdTime = models.DateTimeField(auto_now_add=True, verbose_name="زمان ایجاد")
    changedTime = models.DateTimeField(auto_now=True, verbose_name="زمان تغییر")

    def __str__(self):
        return "{0}".format(self.category_name)


@python_2_unicode_compatible
class ProviderQuestions(models.Model):
    class Meta:
        verbose_name = "سوالات سرویس دهندگان"
        verbose_name_plural = "سوالات سرویس دهندگان"

    category_name = models.ForeignKey(ProviderCategory, on_delete=models.CASCADE, verbose_name="انتخاب دسته")
    question_name = models.CharField(max_length=200, null=False, blank=False, verbose_name="عنوان سوال")
    question_answer = models.CharField(max_length=2000, verbose_name="پاسخ سوال")
    question_priority = models.CharField(max_length=100, verbose_name="اولویت",
                                         choices=choice_list)
    createdTime = models.DateTimeField(auto_now_add=True, verbose_name="زمان ایجاد")
    changedTime = models.DateTimeField(auto_now=True, verbose_name="آخرین تغییر")

    def __str__(self):
        return "{0}_{1}".format(self.question_priority, self.question_name)


@python_2_unicode_compatible
class UserInformation(models.Model):
    class Meta:
        verbose_name = "کاربران تلگرام بات"
        verbose_name_plural = "کاربران تلگرام بات"

    user_id = models.CharField(max_length=50, verbose_name="کد کاربری تلگرام", unique=True)
    username = models.CharField(max_length=50, verbose_name="نام انتخابی کاربر")
    first_name = models.CharField(max_length=50, verbose_name="نام کاربر")
    last_name = models.CharField(max_length=50, verbose_name="فامیل کاربر")
    createdUserTime = models.DateTimeField(auto_now_add=True, verbose_name="زمان ساخت اکانت")
    changedUserTime = models.DateTimeField(auto_now=True, verbose_name="آخرین استفاده از ربات")
    status = models.CharField(max_length=200, choices=[('فعال', 'فعال'), ('غیرفعال', 'غیرفعال')],
                              default="فعال", verbose_name="وضعیت کاربر")
    state = models.CharField(default="جدید", max_length=200, verbose_name="موقعیت در ربات")
    account_type = models.CharField(max_length=200, choices=[('ناظر', 'ناظر'), ('کاربر عادی', 'کاربر عادی')],
                                    default='کاربر عادی', verbose_name="نوع اکانت")

    def __str__(self):
        return "{0}_{1}_{2}_{3}".format(self.user_id, self.username, self.first_name, self.last_name,
                                        self.createdUserTime, self.changedUserTime)


@python_2_unicode_compatible
class UsersLog(models.Model):
    class Meta:
        verbose_name = 'لاگ های کاربران'
        verbose_name_plural = 'لاگ های کاربران'

    user_id = models.CharField(max_length=20, verbose_name="کد کاربری تلگرام")
    user_log_data = models.TextField(verbose_name="لاگ کاربر")
    user_log_time = models.DateTimeField(auto_now=True, verbose_name="زمان لاگ")
    user_log_message_id = models.CharField(max_length=100, verbose_name="شماره پیام")

    def __str__(self):
        return "{0}_{1}_{2}_{3}".format(self.id, self.user_id, self.user_log_data, self.user_log_time,
                                        self.user_log_message_id)


@python_2_unicode_compatible
class UsersOpinion(models.Model):
    class Meta:
        verbose_name = 'انتقادها و پیشنهادها'
        verbose_name_plural = 'انتقادها و پیشنهادها'

    user_opinion_id = models.CharField(max_length=20, verbose_name="کد کاربری تلگرام")
    username = models.CharField(max_length=200, verbose_name="کد کاربری شخصی", blank=True, null=True)
    first_name = models.CharField(max_length=200, verbose_name="نام", blank=True, null=True)
    last_name = models.CharField(max_length=200, verbose_name="فامیل", blank=True, null=True)
    user_opinion_text = models.TextField(verbose_name="متن انتقاد و پیشنهاد")
    user_opinion_time = models.DateTimeField(auto_now=True, verbose_name="زمان انتقاد و پیشنهاد")
    opinion_state = models.CharField(max_length=200, choices=(
        ('دیده نشده', 'دیده نشده'), ('دیده شده', 'دیده شده'), ('قبول شده', 'قبول شده'), ('رد شده', 'رد شده'),
        ('انجام شده', 'انجام شده')), default="دیده نشده", verbose_name="وضعیت")

    def __str__(self):
        return "{0}_{1}_{2}".format(self.user_opinion_id, self.user_opinion_text, self.user_opinion_time)


@python_2_unicode_compatible
class UsersAsk(models.Model):
    class Meta:
        verbose_name = 'سوالات از استادکار'
        verbose_name_plural = 'سوالات از استادکار'

    user_id = models.CharField(max_length=20, verbose_name="کد کاربری تلگرام")
    username = models.CharField(max_length=200, verbose_name="کد کاربری شخصی", blank=True, null=True)
    first_name = models.CharField(max_length=200, verbose_name="نام", blank=True, null=True)
    last_name = models.CharField(max_length=200, verbose_name="فامیل", blank=True, null=True)
    ask_text = models.TextField(verbose_name="متن انتقاد و پیشنهاد")
    ask_time = models.DateTimeField(auto_now=True, verbose_name="زمان انتقاد و پیشنهاد")
    ask_state = models.CharField(max_length=200,
                                 choices=(('پاسخ داده‌نشده', 'پاسخ داده‌نشده'), ('پاسخ داده‌شده', 'پاسخ داده‌شده')),
                                 default="پاسخ داده نشده", verbose_name="وضعیت")
    ask_category = models.CharField(max_length=200, choices=(('مشتری', 'مشتری'), ('سرویس‌دهنده', 'سرویس‌دهنده')),
                                    verbose_name="نوع کاربر")

    def __str__(self):
        return "{0}_{1}_{2}_{3}".format(self.username, self.ask_text, self.ask_time, self.ask_category)
