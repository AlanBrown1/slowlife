# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0003_auto_20170410_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='life',
            name='tag',
            field=models.CharField(choices=[('0', '美食'), ('1', '创意'), ('2', '宠物'), ('3', '健康'), ('4', '情感'), ('5', '花草')], max_length=30, verbose_name='标签'),
        ),
    ]