# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-23 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0003_auto_20171221_0003'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='is_expired',
            field=models.BooleanField(default=False, verbose_name='Is expired'),
        ),
    ]