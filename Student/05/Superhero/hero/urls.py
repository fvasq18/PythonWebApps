
from django.contrib import admin
from django.urls import path
from django.urls import path
from hero.views import Superhero,SuperheroCreateView,SuperheroDeleteView,SuperheroDetailView,SuperheroListView,SuperheroUpdateView,SuperheroView
urlpatterns = [
    
    path('', SuperheroView.as_view()),
    path('<int:pk>', SuperheroDetailView.as_view()),

]