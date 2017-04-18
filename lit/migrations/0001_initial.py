# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 14:00
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='标题')),
                ('author', models.CharField(max_length=30, verbose_name='作者')),
                ('publishtime', models.DateTimeField(auto_now_add=True, verbose_name='发布日期')),
                ('updatetime', models.DateTimeField(auto_now=True, verbose_name='更新日期')),
                ('tag', models.CharField(choices=[('0', '名著'), ('1', '美文'), ('2', '诗词'), ('3', '枕书'), ('4', '随笔')], max_length=30, verbose_name='标签')),
                ('status', models.CharField(choices=[('0', '未审核'), ('1', '已审核')], max_length=20, verbose_name='是否审核')),
                ('zan', models.IntegerField(default=0, verbose_name='赞')),
                ('image', models.ImageField(blank=True, null=True, upload_to='music/images', verbose_name='封面')),
                ('content', DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='内容')),
            ],
        ),
    ]
