# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-04-25 15:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('help_app', '0002_job_my_job'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='location',
        ),
    ]
