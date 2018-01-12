# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ping', '0004_auto_20180111_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='service',
            name='status',
            field=models.SmallIntegerField(default=0),
        ),
    ]
