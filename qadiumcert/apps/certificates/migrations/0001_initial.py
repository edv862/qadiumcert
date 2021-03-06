# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-21 03:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('issuer', models.CharField(max_length=200, verbose_name='Issuer')),
                ('expires', models.DateTimeField(verbose_name='Expires')),
            ],
        ),
        migrations.CreateModel(
            name='IpAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200, verbose_name='Address')),
                ('owner', models.CharField(max_length=200, verbose_name='Owner')),
            ],
        ),
        migrations.CreateModel(
            name='Usage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aditional_info', models.CharField(max_length=200, verbose_name='Aditional info')),
                ('certificate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificates.Certificate')),
                ('ip_address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificates.IpAddress')),
            ],
        ),
        migrations.AddField(
            model_name='ipaddress',
            name='certificate',
            field=models.ManyToManyField(through='certificates.Usage', to='certificates.Certificate'),
        ),
    ]
