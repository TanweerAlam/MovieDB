from .models import Movie

def slider_movies(request):
	# movies = Movie.objects.all().order_by('created_at')[0:1]
	movies = Movie.objects.last()
	return {'slider_movie': movies}