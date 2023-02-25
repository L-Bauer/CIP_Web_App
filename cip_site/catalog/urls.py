from django.urls import path
from django.urls import re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cips/', views.CIPListView.as_view(), name='cips'),
    re_path(r'^cip/(?P<pk>\d+)$', views.CIPDetailView.as_view(), name='cip-detail'),
]

