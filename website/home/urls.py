from django.urls import path
from . import views
urlpatterns = [
    path('', views.carga_files),
    path('home', views.homepage, name = 'users'),
]