from django.urls import path
from django.contrib.admin import site
from hero.views import SuperHeroView
from hero.views import SuperHeroDetailView

urlpatterns = [
    path(r'admin/', site.urls),
    path('', SuperHeroView.as_view()),
    path('<int:pk>', SuperHeroDetailView.as_view()),
]