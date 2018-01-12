from django.contrib import admin

from . import models


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name_cn', 'name_en', 'code', 'order')


class RegionAdmin(admin.ModelAdmin):
    list_display = ('name_cn', 'name_en', 'order')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('endpoint', 'code', 'company', 'region')


admin.site.register(models.Company, CompanyAdmin)
admin.site.register(models.Region, RegionAdmin)
admin.site.register(models.Service, ServiceAdmin)
