# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Certificate(models.Model):
    name = models.CharField(
        'Name',
        max_length=200,
    )
    issuer = models.CharField(
        'Issuer',
        max_length=200,
    )
    expires = models.DateTimeField(
        'Expires',
    )
    is_expired = models.BooleanField(
        'Is expired',
        default=False,
    )


class IpAddress(models.Model):
    address = models.CharField(
        'Address',
        max_length=200,
    )
    owner = models.CharField(
        'Owner',
        max_length=200,
    )
    certificate = models.ManyToManyField(
        Certificate,
        through='Usage',
    )


class Usage(models.Model):
    ipaddress_id = models.ForeignKey(
        IpAddress,
    )
    certificate_id = models.ForeignKey(
        Certificate,
    )
    aditional_info = models.CharField(
        'Aditional info',
        max_length=200,
    )
