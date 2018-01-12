# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ping', '0002_auto_20180111_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='code',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
    ]
