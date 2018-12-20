from django.contrib import admin

from . import models


class PromotionAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'link', 'thumbnail', 'order')


admin.site.register(models.Promotion, PromotionAdmin)
