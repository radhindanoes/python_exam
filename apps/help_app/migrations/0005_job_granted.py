# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-04-25 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('help_app', '0004_job_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='granted',
            field=models.BooleanField(default=False),
        ),
    ]
