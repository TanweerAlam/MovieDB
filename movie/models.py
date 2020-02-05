from django.db import models
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.
CATEGORY_CHOICES = (
	('action', 'ACTION'),
	('drama', 'DRAMA'),
	('comedy', 'COMEDY'),
	('romance', 'ROMANCE'),
)

LANGUAGE_CHOICES = (
	('english', 'ENGLISH'),
	('german', 'GERMAN'),
)

STATUS_CHOICES =  (
	('RA', 'RECENTLY ADDED'),
	('MW', 'MOST WATCHED'),
	('TR', 'TOP RATED'),
)

class Movie(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(max_length=1000)
	image = models.ImageField(upload_to='movies')
	banner = models.ImageField(upload_to='movies_banner')
	category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
	language = models.CharField(choices=LANGUAGE_CHOICES, max_length=10)
	status = models.CharField(choices=STATUS_CHOICES, max_length=2)
	cast = models.CharField(max_length=100, default='')
	year_of_production = models.DateField()
	views_count = models.IntegerField(default=0)

	movie_trailer = models.URLField(default='')
	slug = models.SlugField(max_length=120, blank=True, null=True)

	created_at = models.DateTimeField(default=timezone.now)


	# -tags
	# -download links
	# -watch links
	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super(Movie, self).save(*args, **kwargs)

	def __str__(self):
		return self.title


LINK_CHOICES = (
	('D', 'DOWNLOAD LINK'),
	('W', 'WATCH LINK'),
)

class MovieLinks(models.Model):
	movie = models.ForeignKey(Movie, related_name='movie_watch_link', on_delete=models.CASCADE)
	type_of_link = models.CharField(choices= LINK_CHOICES, max_length=1)
	link = models.URLField()

	def __str__(self):
		return str(self.movie)