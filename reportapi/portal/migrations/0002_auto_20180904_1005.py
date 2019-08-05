# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-09-04 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.CharField(blank=True, max_length=100, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='img')),
                ('system_date', models.DateField(auto_now=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='AllocationStatus',
        ),
        migrations.DeleteModel(
            name='Bin',
        ),
        migrations.DeleteModel(
            name='BinsMovement',
        ),
        migrations.DeleteModel(
            name='BinsReceipt',
        ),
        migrations.DeleteModel(
            name='BinStatus',
        ),
        migrations.DeleteModel(
            name='BinType',
        ),
        migrations.DeleteModel(
            name='ClientBinAllocation',
        ),
        migrations.DeleteModel(
            name='ClientRewards',
        ),
        migrations.DeleteModel(
            name='Clients',
        ),
        migrations.DeleteModel(
            name='Collector',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Complaints',
        ),
    ]
