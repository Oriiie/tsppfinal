from django import template
from movies.models import Category, Movie


register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('movies/tags/last_movie.html')
def get_last_movies():
    movies = Movie.objects.order_by("id")[len(Movie.objects.all())-5:len(Movie.objects.all()):-1]
    return {"last_movies": movies}
