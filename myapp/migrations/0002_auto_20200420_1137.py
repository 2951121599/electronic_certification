# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-04-20 03:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(default=0, max_length=50, null=True, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='user',
            name='image_name',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='真实姓名'),
        ),
        migrations.AlterField(
            model_name='user',
            name='img_gender',
            field=models.CharField(default='', max_length=50, verbose_name='图片上性别'),
        ),
        migrations.AlterField(
            model_name='user',
            name='img_img',
            field=models.CharField(default='', max_length=50, null=True, verbose_name='图片信息'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, verbose_name='用户名'),
        ),
    ]
