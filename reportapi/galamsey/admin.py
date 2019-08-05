from __future__ import unicode_literals

from django.contrib import admin

from .models import *
# Register your models here.


class incidentReportsAdmin(admin.ModelAdmin):
    list_display = ('Description','image','voice','lat','lng')





admin.site.register(incidentReports, incidentReportsAdmin)
