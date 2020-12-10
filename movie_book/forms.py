from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ['name', 'directing', 'genre_name']