# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-11 07:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_auto_20170410_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='content',
            field=models.TextField(verbose_name='内容'),
        ),
    ]
