# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-11 07:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_music_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='content',
            field=models.TextField(verbose_name='内容'),
        ),
    ]
