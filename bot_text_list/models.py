from django.db import models
from future.utils import python_2_unicode_compatible


@python_2_unicode_compatible
class TelegramTextCategory(models.Model):
    class Meta:
        verbose_name = 'دسته بندی عمومی متون'
        verbose_name_plural = 'دسته بندی عمومی متون'

    category_get = models.TextField(blank=False, null=False, verbose_name="دسته")

    def __str__(self):
        return str(self.category_get)


@python_2_unicode_compatible
class TelegramState(models.Model):
    class Meta:
        verbose_name = 'موقعیت در ربات'
        verbose_name_plural = 'موقعیت در ربات'

    state_name = models.TextField(verbose_name="موقعیت", default="state_new")
    state_description = models.CharField(max_length=200, verbose_name="توضیح موقعیت", default="جدید")

    def __str__(self):
        return "{0}".format(self.state_description)


@python_2_unicode_compatible
class TelegramText(models.Model):
    class Meta:
        verbose_name = 'متن های عمومی ربات'
        verbose_name_plural = 'متن های عمومی ربات'

    category_get = models.OneToOneField(TelegramTextCategory, on_delete=models.CASCADE, verbose_name="دسته بندی")
    text_get = models.TextField(verbose_name="متن")

    def __str__(self):
        return "{0}_{1}".format(self.category_get, self.text_get)
