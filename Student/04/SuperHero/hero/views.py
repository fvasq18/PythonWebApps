from django.views.generic.list import ListView
from .models import Superhero
from django.views.generic.detail import DetailView

class SuperHeroView(ListView):
    template_name = 'index.html'
    model = Superhero

class SuperHeroDetailView(DetailView):
    template_name='hero_detail.html'
    model = Superhero

