from django.shortcuts import render, redirect
from django.views import generic

from .models import Movie
from .forms import MovieForm


class MovieIndex(generic.ListView):

    template_name = 'movie_book/movie_index.html'
    context_object_name = 'Movies'

    def get_queryset(self):
        return Movie.objects.all().order_by('-id')


class CurrentMovieView(generic.DeleteView):

    model = Movie
    template_name = 'movie_book/movie_detail.html'


class CreateMovie(generic.edit.CreateView):

    form_class = MovieForm
    template_name = 'movie_book/create_movie.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return render(request, self.template_name, {'form':form})
