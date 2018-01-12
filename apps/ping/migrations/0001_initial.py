# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_cn', models.CharField(max_length=30, null=True)),
                ('name_en', models.CharField(max_length=30, null=True)),
                ('link', models.CharField(max_length=100)),
                ('order', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_cn', models.CharField(max_length=30, null=True)),
                ('name_en', models.CharField(max_length=30, null=True)),
                ('description', models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('endpoint', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=30)),
            ],
        ),
    ]
