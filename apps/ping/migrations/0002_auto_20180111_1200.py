# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ping', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='company',
            field=models.ForeignKey(default=None, to='ping.Company'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='region',
            field=models.ForeignKey(default=None, to='ping.Region'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='name_cn',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='name_en',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='description',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='name_cn',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='name_en',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
