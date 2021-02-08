from django.urls import path
from . import views


urlpatterns = [
    path('',views.inicio, name='home'),
    path('respuesta/',views.respuesta, name='respuesta'),
]