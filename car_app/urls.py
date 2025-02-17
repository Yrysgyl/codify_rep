from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  
    path('car_create/', views.car_create_view, name='car_create'),
]
