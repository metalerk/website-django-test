# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-02 01:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20161124_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='preview',
            field=models.CharField(default='Lorem Ipsum dolor', max_length=500),
            preserve_default=False,
        ),
    ]
