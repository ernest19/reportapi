# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-08 18:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_auto_20180904_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='report_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]