from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from .views import *
from rest_framework import renderers


Report_list = ReportViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
Report_detail = ReportViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
Report_highlight = ReportViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])


charcoalReport_list = charcoalReportViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
charcoalReport_detail = charcoalReportViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
charcoalReport_highlight = charcoalReportViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])



user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})





urlpatterns = format_suffix_patterns([
    url(r'^$', api_root),

    url(r'^charcoalreport/$', charcoalReport_list, name='snippet-list'),
    url(r'^charcoalreport/(?P<pk>[0-9]+)/$', charcoalReport_detail, name='snippet-detail'),
    url(r'^charcoalreport/(?P<pk>[0-9]+)/highlight/$', charcoalReport_highlight, name='Client_highlight'),


    url(r'^report/$', Report_list, name='snippet-list'),
    url(r'^report/(?P<pk>[0-9]+)/$', Report_detail, name='snippet-detail'),
    url(r'^report/(?P<pk>[0-9]+)/highlight/$', Report_highlight, name='Client_highlight'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
])








urlpatterns = [
 url(r'^client/$', ClientViewSet.as_view(), name="create"),
]