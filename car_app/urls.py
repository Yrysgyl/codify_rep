from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),  
    path('car_create/', views.car_create_view, name='car_create'),
    path('car_create_2/', views.car_create_view_2),
    path('car_detail/<int:pk>/', views.car_detail_view, name='detail'),
    path('car_detail_2/<int:pk>/', views.car_detail_view_2, name='detail_2'),
    path('car_delete/<int:pk>/', views.car_delete_view, name='delete')
]
