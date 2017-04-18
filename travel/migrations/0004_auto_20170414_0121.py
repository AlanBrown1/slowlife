# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-13 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_auto_20170411_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='image',
            field=models.ImageField(blank=True, help_text='图像尺寸：192*128', null=True, upload_to='travel/images', verbose_name='封面'),
        ),
    ]
