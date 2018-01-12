# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ping', '0003_auto_20180111_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='code',
            field=models.CharField(max_length=30),
        ),
    ]
