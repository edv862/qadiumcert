# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-21 03:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usage',
            old_name='ip_address_id',
            new_name='certificate',
        ),
        migrations.RenameField(
            model_name='usage',
            old_name='certificate_id',
            new_name='ip_address',
        ),
    ]
