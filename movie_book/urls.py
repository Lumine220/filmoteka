from django.urls import path
from . import views

urlpatterns = [
    path('movie_index/', views.MovieIndex.as_view(), name='movie_index'),
    path('<int:pk>/movie_detail', views.CurrentMovieView.as_view(), name='movie_detail'),
    path('create_movie/', views.CreateMovie.as_view(), name='new_movie')
]