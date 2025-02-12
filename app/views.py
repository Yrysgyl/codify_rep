from django.shortcuts import render, get_object_or_404
from .models import Music

def music_list(request):
    """Отображение списка песен"""
    musics = Music.objects.all()
    return render(request, 'app/music_list.html', {'musics': musics})

def music_detail(request, music_id):
    """Детальный просмотр песни с возможностью прослушивания"""
    music = get_object_or_404(Music, pk=music_id)
    return render(request, 'app/music_detail.html', {'music': music})

