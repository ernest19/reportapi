# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-07-21 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galamsey', '0002_incidentreports'),
    ]

    operations = [
        migrations.AddField(
            model_name='incidentreports',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]