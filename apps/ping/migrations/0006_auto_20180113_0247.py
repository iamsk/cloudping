# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ping', '0005_auto_20180112_0422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='link',
            field=models.CharField(max_length=300),
        ),
    ]
