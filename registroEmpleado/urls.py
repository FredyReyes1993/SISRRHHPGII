from django.urls import path
from . import views
from django.contrib import admin


urlpatterns = [   
    path('registroEm', views.registroEm, name='registroEm'),
]