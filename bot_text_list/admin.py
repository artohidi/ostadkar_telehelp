from django.contrib import admin
from .models import TelegramTextCategory, TelegramText, TelegramState


class TelegramStateAdmin(admin.ModelAdmin):
    list_display = ('id', 'state_name', 'state_description')
    ordering = ('id',)


class TelegramTextCategoryAdmin(admin.ModelAdmin):
    # readonly_fields = ['category_get']
    ordering = ('id',)
    list_display = ('id', 'category_get')


class TelegramTextAdmin(admin.ModelAdmin):
    list_display = ("category_get", "text_get")
    ordering = ('category_get',)
    list_display_links = ('category_get',)


admin.site.register(TelegramState, TelegramStateAdmin)
admin.site.register(TelegramTextCategory, TelegramTextCategoryAdmin)
admin.site.register(TelegramText, TelegramTextAdmin)
