# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-09-10 21:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180910_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 10, 21, 15, 48, 111646, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 10, 21, 15, 48, 110649, tzinfo=utc)),
        ),
    ]
