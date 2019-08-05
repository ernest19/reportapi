# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-07-22 05:19
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galamsey', '0003_incidentreports_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidentreports',
            name='gps_coordinates_geom',
            field=django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326),
        ),
    ]