from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cips/', views.CIPListView.as_view(), name='cips'),
]
