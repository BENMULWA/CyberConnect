from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('review--<str:token>/', views.review_detail, name='review_detail'), # the name review is the one that is mapped in the navbar on base.html and the link review--jpkeg>123 is the one that hundles the url that user sees after clicks 
    path('about/', views.about_view, name='about'),
    path('services/', views.services_view, name='services'),
    path('careers/', views.careers_view, name='careers'),
    path('know_more/', views.know_more_view, name='know_more'),
    path('services/ecitizen/', views.ecitizen_detail, name='ecitizen_detail'),
]
