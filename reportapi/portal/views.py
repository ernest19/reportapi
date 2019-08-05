
import os

from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import *
from galamsey.models import *
import requests
from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import *
from rest_framework import filters
import django_filters


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response




class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers

    filter_backends = (filters.OrderingFilter ,filters.SearchFilter)
    filter_fields = ('username',)
    ordering =('-id',)
    search_fields = ('last_name','username')


# class ReportViewSet(viewsets.ModelViewSet):
#     queryset = Report.objects.all()
#     serializer_class = ReportSerializers

#     filter_backends = (filters.OrderingFilter ,filters.SearchFilter)
#     filter_fields = ('Description',)
#     ordering =('-id',)
#     search_fields = ('longitude','latitude','report_type')


class ReportViewSet(viewsets.ModelViewSet):
    queryset = incidentReports.objects.all()
    serializer_class = ReportSerializers

    filter_backends = (filters.OrderingFilter ,filters.SearchFilter)
    filter_fields = ('report',)
    ordering =('-id',)
    search_fields = ('status','lat','lng')



class charcoalReportViewSet(viewsets.ModelViewSet):
    queryset = charcoalReports.objects.all()
    serializer_class = charcoalSerializers

    filter_backends = (filters.OrderingFilter ,filters.SearchFilter)
    filter_fields = ('report',)
    ordering =('-id',)
    search_fields = ('status','lat','lng')

# class BinViewSet(viewsets.ModelViewSet):
#     queryset = Bin.objects.all()
#     serializer_class = BinSerializers

#     filter_backends = (filters.OrderingFilter ,filters.SearchFilter)
#     filter_fields = ('bin_code',)
#     ordering =('-id',)
#     search_fields = ('bin_code','bin_name')




