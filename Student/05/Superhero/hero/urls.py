
from django.contrib import admin
from django.urls import path
from django.urls import path
from hero.views import Superhero,SuperheroCreateView,SuperheroDeleteView,SuperheroDetailView,SuperheroListView,SuperheroUpdateView
urlpatterns = [
    
    path('', SuperheroListView.as_view()),
    path('<int:pk>', SuperheroDetailView.as_view()),            
    path('blog/add', SuperheroCreateView.as_view(),  name='blog_add'),
    path('blog/<int:pk>/', SuperheroUpdateView.as_view(),  name='blog_edit'),
    path('blog/<int:pk>/delete', SuperheroDeleteView.as_view(),  name='blog_delete'),

]