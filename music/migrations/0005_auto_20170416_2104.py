# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-16 13:04
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20170414_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='content',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='内容'),
        ),
    ]
