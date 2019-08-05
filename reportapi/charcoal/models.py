# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models

from django.utils import timezone

from django.contrib.gis.geos import GEOSGeometry


class fcm_info(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField()
    date_created = models.DateTimeField(blank=True, null=True)
    device_id = models.CharField(max_length=150, blank=True, null=True)
    registration_id = models.TextField()
    type = models.CharField(max_length=10)
    # user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fcm_django_fcmdevice'



# class incidentReports(models.Model):
# 	Description = models.CharField(max_length=2500, blank=True, null=True)
# 	status = models.CharField(max_length=2500, blank=True, null=True)
# 	image = models.ImageField(upload_to="galamsey/pic/", null=True)
# 	voice=models.FileField(upload_to='galamsey/audio/', null=True)
# 	lat = models.FloatField(default=0)
# 	lng = models.FloatField(default=0)
# 	geom =models.GeometryField(blank=True, null=True)
# 	created_date = models.DateTimeField(auto_now=True)

# 	def save(self, *args, **kwargs):
# 		if self.lng:
# 			if float(self.lng) != 0:
# 				point = 'MultiPoint (' + str(self.lng) +' '+ str(self.lat) +')'
# 				point = GEOSGeometry(point)
# 				self.geom  = point
# 			super(incidentReports, self).save(*args, **kwargs)    


class charcoalReports(models.Model):
	Description = models.CharField(max_length=2500, blank=True, null=True)
	status = models.CharField(max_length=2500, blank=True, null=True)
	image = models.ImageField(upload_to="charcoal/pic/", null=True)
	voice=models.FileField(upload_to='charcoal/audio/', null=True)
	lat = models.FloatField(default=0)
	lng = models.FloatField(default=0)
	geom =models.GeometryField(blank=True, null=True)
	created_date = models.DateTimeField(auto_now=True)

	def save(self, *args, **kwargs):
		if self.lng:
			if float(self.lng) != 0:
				point = 'MultiPoint (' + str(self.lng) +' '+ str(self.lat) +')'
				point = GEOSGeometry(point)
				self.geom  = point
			super(charcoalReports, self).save(*args, **kwargs)    
