from django.shortcuts import render


def index(request):
    return render(request, "movie_book/index.html", dict(movie_name="Guardians of the Galaxy", genre='sci-fi', score='7/10'))
