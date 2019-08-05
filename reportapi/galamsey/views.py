# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import  ast
import datetime
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
from django.contrib.gis.db.models import Extent
from djgeojson.views import GeoJSONLayerView
from .models import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pyfcm import FCMNotification






def index(request):
	toHTML = {}

	return render(request, 'index.html', toHTML)



@csrf_exempt
def fcm_insert(request): 
    token = request.GET.get("fcm_token")
    if not fcm_info.objects.filter(registration_id = token ):
      ad=fcm_info()
      ad.device_id = "zvxcvxcvx"
      ad.registration_id= token  
      ad.active=True
      # ad.device_id

      ad.save()
      return HttpResponse(token)
    else:
      return HttpResponse("already Exist ")


def send_notifications(request): 
  path_to_fcm = "https://fcm.googleapis.com"
  server_key = 'AAAA-5Vy9ug:APA91bF63BZ6QP2ZJpTRIjoU3GZE9_yy1m3tqWfKv7Y9STxh0YYH9mTU7UxSMd-r-0hS527ldqgWpPuFx9LOCbP8V6j8zfxUgQ99K7TdQvpPChrHWoq2eUXdt7qzCAeGzdXHbJM44ays'
  reg_id = fcm_info.objects.all() #quick and dirty way to get that ONE fcmId from table

  for aa in reg_id:

    
    message_title = "GALAMSEY APP- Notifications"
    message_body = "There are 45 galamsey site confirm in Wassa Amenfi"
    result = FCMNotification(api_key=server_key).notify_single_device(registration_id=aa.registration_id, message_title=message_title, message_body=message_body)
    print reg_id.count()
    print result
  return HttpResponse(result)


def alertView(request):
	toHTML = {}
	dt =  datetime.datetime.now()

	toHTML["current"]= dt  

	toHTML["alert"]=incidentReports.objects.all().order_by("-created_date")

  # toHTML["alert"]=incidentReports.objects.filter(created_date__date = dt.strftime("%Y-%m-%d")  )
	return render(request, 'alert.html', toHTML)
















class RegionBoundarylayerView(GeoJSONLayerView):
  model = RegionalBoundary
  precision = 4   
  simplify = 0.01
  properties = ('region',)


class DistrictGeojsonView(GeoJSONLayerView):
    model = District
    precision = 4
    properties = ('district_name','district_pop','employment_pop')



# class incidentReportspointView(GeoJSONLayerView):
#   model = incidentReports
#   precision =  4
#   properties = ('Description','image','voice','created_date')





def topolygon(resulpoygon):
  mainjson = []
  mainjson.append({"crs":{"type":"link","properties": {"href":"http://spatialreference.org/ref/epsg/4326/","type":"proj4"}},"type":"FeatureCollection","features":resulpoygon})
  return mainjson



def returnsimplify(geom,simplifyvalue=0.01):
  # return geom.simplify(simplifyvalue, preserve_topology=True).geojson
  return geom.simplify(simplifyvalue).geojson



def incidentReportspointView(request):
  resulpoygon = []
  incident=incidentReports.objects.all()
  for aa in incident:
    description=aa.Description
    image=aa.image
    voice=aa.voice
    created_date=aa.created_date
    status=aa.status
   

    try:
    
      resulpoygon.append({"geometry":ast.literal_eval(returnsimplify(aa.geom)),"type":"Feature","properties":{'description':description,'image':str(image),'voice':str(voice),'created_date':created_date,'status':status}})
    except Exception as e:
     raise
      # saljson=topolygon(resulpoygon)
  return JsonResponse(topolygon(resulpoygon),safe=False)




def ExtentView(request):
  valuecode = request.GET.get('valuecode')
  
  tojson = incidentReports.objects.filter(id=valuecode).aggregate(Extent('geom')).get('geom__extent')
    
  return JsonResponse(tojson,safe = False)































# class incidentReportsViewSet(viewsets.ModelViewSet):
#     queryset = incidentReports.objects.all()
#     serializer_class = incidentReportsSerializer

#     # filter_backends = (filters.OrderingFilter ,filters.SearchFilter)
#     # filter_fields = ('report',)
#     ordering =('-id',)
#     # search_fields = ('longitude','latitude','report_type')




# class incidentReportsViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = incidentReports.objects.all().order_by('-created_date')
#     serializer_class = incidentReportsSerializer


# @api_view(['GET', 'POST'])
# def incidentReportsView(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         incident = incidentReports.objects.all()
#         serializer = incidentReportsSerializer(incident, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = incidentReportsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)