# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-21 07:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('introapp', '0006_auto_20160120_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='set_password',
        ),
    ]
