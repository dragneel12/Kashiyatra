# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-28 07:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_auto_20170624_0158'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SignUp',
        ),
    ]
