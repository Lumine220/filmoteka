from django.db import models


class Genre(models.Model):
    genre = models.CharField(max_length=80)

    def __str__(self):
        return f'Genre: {self.genre}'


class Movie(models.Model):
    name = models.CharField(max_length=200)
    directing = models.CharField(max_length=180)
    genre_name = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, verbose_name='Genre')

    def __str__(self):
        return f'Movie: {self.name} | Directing: {self.directing} | Genre: {self.genre_name}'
