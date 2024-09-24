from django.urls import path
from .views import SpidermanView, BatmanView, IndexView, SuperManView, FlashView, BlackPantherView

urlpatterns = [
    path('', IndexView.as_view()),
    path('spiderman', SpidermanView.as_view()),
    path('batman', BatmanView.as_view()),
    path('superman', SuperManView.as_view()),
    path('flash',FlashView.as_view()),
    path('blackpanther', BlackPantherView.as_view())
]
