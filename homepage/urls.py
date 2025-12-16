# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    
    # Static sections
    path('about/', views.about_entry, name='about'),
    path('about/<str:token>/', views.about_detail, name='about_detail'),
    
    path('reviews/', views.reviews_entry, name='review'),
    path('reviews/<str:token>/', views.reviews_detail, name='reviews_detail'),
    
    path('careers/', views.careers_entry, name='careers'),
    path('careers/<str:token>/', views.careers_detail, name='careers_detail'),
    
    path('know-more/', views.know_more_entry, name='know_more'),
    path('know-more/<str:token>/', views.know_more_detail, name='know_more_detail'),
    
    # Services path('services/book/<int:service_id>/', views.book_service, name='book_service'),
    path('services/', views.services_entry, name='services'),
    path('services/<str:token>/', views.services_detail, name='services_detail'),
    path('services/detail/<int:service_id>/', views.service_detail, name='service_detail'),
    
    
    # eCitizen
    path('ecitizen/', views.ecitizen_entry, name='ecitizen_detail'),
    path('ecitizen/<str:token>/', views.ecitizen_detail, name='ecitizen_detail'),
    
    # Cart
    path('cart/', views.view_cart, name='view_cart'),
    path('cart/update/<int:service_id>/', views.update_cart, name='update_cart'),
    path('cart/remove/<int:service_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    
]