from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('know_more/', views.know_more_view, name='know_more'),
    path('services/ecitizen/', views.ecitizen_detail, name='ecitizen_detail'),
]
