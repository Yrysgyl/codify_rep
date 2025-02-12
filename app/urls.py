from django.urls import path
from .views import music_list, music_detail

urlpatterns = [
    path('', music_list, name='music_list'),
    path('<int:music_id>/', music_detail, name='music_detail'),
]
