# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-16 12:03
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('life', '0006_auto_20170414_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='life',
            name='content',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='内容'),
        ),
    ]