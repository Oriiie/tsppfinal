from django.test import TestCase
from .models import *
from django.core.files.uploadedfile import SimpleUploadedFile


# Create your tests here.


class MovieTestCase(TestCase):

    def setUp(self) -> None:
        self.movie = Movie.objects.create(
            title='Movie1',
            tagline='tagline1',
            description='description1',
            poster=SimpleUploadedFile("poster.jpg", content=b'', content_type="image/jpg"),
            year=2020,
            country='USA',
            world_premiere=date.today(),
            budget=1000000,
            fees_in_usa=20000000,
            fees_in_world=50000000,
            url='movieurl',
            draft=True
        )

    def test_movie(self):
        self.assertEquals(self.movie.title, 'Movie1')
        self.assertEquals(self.movie.tagline, 'tagline1')
        self.assertEquals(self.movie.description, 'description1')
        self.assertEquals(self.movie.year, 2020)
        self.assertEquals(self.movie.country, 'USA')
        self.assertEquals(self.movie.world_premiere, date.today())
        self.assertEquals(self.movie.budget, 1000000)
        self.assertEquals(self.movie.fees_in_usa, 20000000)
        self.assertEquals(self.movie.fees_in_world, 50000000)
        self.assertEquals(self.movie.url, 'movieurl')
        self.assertEquals(self.movie.draft, True)

    def test_name(self):
        self.assertLess(len(self.movie.title), 100)

    def test_description(self):
        self.assertLess(len(self.movie.description), 512)

    def test_year(self):
        self.assertGreater(self.movie.year, 1850)

    def test_country(self):
        self.assertLess(len(self.movie.country), 60)


class ActorTestCase(TestCase):
    def setUp(self) -> None:
        self.actor = Actor.objects.create(
            name='actor',
            age=50,
            description='desc',
            image=SimpleUploadedFile("image.jpg", content=b'', content_type="image/jpg")
        )

    def test_actor(self):
        self.assertEquals(self.actor.name, 'actor')
        self.assertEquals(self.actor.age, 50)
        self.assertEquals(self.actor.description, 'desc')

    def test_description(self):
        self.assertLess(len(self.actor.description), 1)


class GenreTestCase(TestCase):
    def setUp(self) -> None:
        self.genre = Genre.objects.create(
            name='genre',
            description='desc',
            url='genre'
        )

    def test_genre(self):
        self.assertEquals(self.genre.name, 'genre')
        self.assertEquals(self.genre.description, 'desc')
        self.assertEquals(self.genre.url, 'genre')

    def test_description(self):
        self.assertLess(len(self.genre.description), 512)

