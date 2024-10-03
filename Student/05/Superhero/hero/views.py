from django.shortcuts import render
from .models import Superhero
from django.views.generic import CreateView, DeleteView,ListView,UpdateView, DetailView

# Create your views here.


class SuperheroCreateView(CreateView):
    template_name = "add.html"
    model = Superhero
    fields = "__all__"
class SuperheroDeleteView(DeleteView):
    model = Superhero
    template_name = 'delete.html'
class SuperheroListView(ListView):
    template_name = 'index.html'
    model = Superhero
    context_object_name = 'heros'
class SuperheroUpdateView(UpdateView):
    template_name = "edit.html"
    model = Superhero
    fields = '__all__'
class SuperheroDetailView(DetailView):
    template_name = 'detail.html'
    model = Superhero
    context_object_name = 'hero'