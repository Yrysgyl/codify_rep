from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),  
    path('car_create/', views.car_create_view, name='car_create'),
    path('car_create_2/', views.car_create_view_2),
]
