from django.urls import path
#from recipes.views import home, sobre, contato
from . import views

# HTTP Request
urlpatterns = [
    path('', views.home),
    path('recipe/<int:id>/', views.recipe),
]
