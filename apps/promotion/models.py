from django.db import models

from apps.ping.models import Company


class Promotion(models.Model):
    title = models.CharField(max_length=100)
    company = models.ForeignKey(Company)
    link = models.CharField(max_length=300)
    thumbnail = models.CharField(max_length=300, null=True, blank=True)
    order = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.title
