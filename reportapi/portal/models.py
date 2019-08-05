# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class Report(models.Model):
	report_type = models.CharField(max_length=100, blank=True, null=True)
	report = models.CharField(max_length=100, blank=True, null=True)
	longitude = models.FloatField(blank=True, null=True)
	latitude = models.FloatField(blank=True, null=True)
	image = models.ImageField(upload_to='img', blank=True, null=True)
	system_date =  models.DateField(auto_now=True ,blank=True, null=True, editable=False)



class charcoalReport(models.Model):
	report_type = models.CharField(max_length=100, blank=True, null=True)
	report = models.CharField(max_length=100, blank=True, null=True)
	longitude = models.FloatField(blank=True, null=True)
	latitude = models.FloatField(blank=True, null=True)
	image = models.ImageField(upload_to='charcoal/img', blank=True, null=True)
	system_date =  models.DateField(auto_now=True ,blank=True, null=True, editable=False)



