# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2019-07-31 08:42
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='fcm_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('active', models.BooleanField()),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('device_id', models.CharField(blank=True, max_length=150, null=True)),
                ('registration_id', models.TextField()),
                ('type', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'fcm_django_fcmdevice',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='charcoalReports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(blank=True, max_length=2500, null=True)),
                ('status', models.CharField(blank=True, max_length=2500, null=True)),
                ('image', models.ImageField(null=True, upload_to='charcoal/pic/')),
                ('voice', models.FileField(null=True, upload_to='charcoal/audio/')),
                ('lat', models.FloatField(default=0)),
                ('lng', models.FloatField(default=0)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('created_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='incidentReports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(blank=True, max_length=2500, null=True)),
                ('status', models.CharField(blank=True, max_length=2500, null=True)),
                ('image', models.ImageField(null=True, upload_to='galamsey/pic/')),
                ('voice', models.FileField(null=True, upload_to='galamsey/audio/')),
                ('lat', models.FloatField(default=0)),
                ('lng', models.FloatField(default=0)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('created_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]