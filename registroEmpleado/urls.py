from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [   
    path('registroEmpleado/', views.gestionEmpleados, name='gestionEmpleados'),
    path('registroEm', views.registroEm, name='registroEm'),
]