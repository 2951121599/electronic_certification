# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-04-30 04:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20200420_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('0', '未通过'), ('1', '通过')], default='未通过', max_length=50, verbose_name='审核状态'),
        ),
    ]
