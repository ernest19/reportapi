# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-07-26 12:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galamsey', '0008_auto_20190726_0439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidentreports',
            name='voice',
            field=models.FileField(null=True, upload_to='galamsey/audio/'),
        ),
    ]