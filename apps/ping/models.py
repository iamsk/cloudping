from django.db import models


class Company(models.Model):
    name_en = models.CharField(max_length=30, null=True, blank=True)
    name_cn = models.CharField(max_length=30, null=True, blank=True)
    code = models.CharField(max_length=30)
    link = models.CharField(max_length=300)
    order = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name_en or self.name_cn


class Region(models.Model):
    name_en = models.CharField(max_length=30, null=True, blank=True)
    name_cn = models.CharField(max_length=30, null=True, blank=True)
    order = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name_en or self.name_cn


class Service(models.Model):
    endpoint = models.CharField(max_length=100)
    code = models.CharField(max_length=30)
    company = models.ForeignKey(Company)
    region = models.ForeignKey(Region)
    status = models.SmallIntegerField(default=0)

    def __unicode__(self):
        return self.endpoint
