from django.conf.urls import url,include
from . import views

from rest_framework import renderers
from rest_framework import routers
from .views import *
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static









urlpatterns = [



	 url(r'fcm_inserturl/$', views.fcm_insert, name='cofdata'),
	 url(r'send/', views.send_notifications, name='send') ,
    
     url(r'^$', views.index, name='index'),
     # url(r'^regionboundary/(?P<typevalue>[A-Z0-9]+)/$', views.RegionBoundarylayerView.as_view(),name='regionjson'),
   
     url(r'^regionboundary/(?P<typevalue>[A-Z0-9]+)/$', views.RegionBoundarylayerView.as_view(),name='regionjson'),

 	 url(r'district/$', views.DistrictGeojsonView.as_view(), name='district'),
 	 
     # url('api', include(router.urls)),
    # url('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
   

     # url(r'incidentapi/$', views.incidentReportsView, name='map'),

     url(r'alert/$', views.alertView, name='alertviewapi'),        

	url(r'^extenta/$', views.ExtentView, name='extenta'),

     url(r'incidentreportspoint/$', views.incidentReportspointView, name='incidentReportspoint'),    


 ]















