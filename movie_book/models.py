from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=200)
    directing = models.CharField(max_length=180)

    def __str__(self):
        return f"Movie name: {self.name} | Directing: {self.directing}"


class Genre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.CharField(max_length=80)

    def __str__(self):
        return f"Movie: {self.movie} | Genre: {self.genre}"
