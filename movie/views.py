from django.shortcuts import get_object_or_404, render
from movie.models import Movie

def movie_list(request):
    movies = Movie.objects.all()
    
    return render(request, 'movie/index.html', {'movies': movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    
    return render(request, 'movie/detail.html', {'movie': movie})
