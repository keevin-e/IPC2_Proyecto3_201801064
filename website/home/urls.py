from django.urls import path
from . import views
urlpatterns = [
    path('', views.carga_files, name= 'carga_files' ),
    path('consulta', views.consulta_page),
    path('view-catg', views.consulta_Categorias, name = 'categorias'),
    path('view-clientes', views.consulta_clientes, name = 'clientes'),
    path('view-recursos', views.consulta_recursos, name = 'recursos'),
    path('creacion', views.creacion_page),
    path('crear_recurso', views.crear_recurso),
]