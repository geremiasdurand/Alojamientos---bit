from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    #Se llaman a las funciones de views.py y se les registra un link
    #Los valores con <int:pk> trabajan con un parametro para obtener
    #datos de la base de datos distintos
    path('', views.alojamiento_list, name='alojamiento_list'),
    path('<int:pk>/', views.alojamiento_detail, name='alojamiento_detail'),
    path('nuevo', views.alojamiento_new, name='alojamiento_new'),
    path('editar/<int:pk>/', views.alojamiento_edit, name='alojamiento_editar'),
    url(r'^(?P<pk>\d+)/comentario/$', views.añadir_comentario, name='añadir_comentario'),
    path('eliminar/<int:pk>', views.alojamiento_delete, name="alojamiento_delete"),
    path('eliminar_comentario/<int:pk>', views.eliminar_comentario, name="eliminar_comentario"),
]
