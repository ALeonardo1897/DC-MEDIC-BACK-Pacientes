
from django.contrib import admin
from django.urls import path, include

#Rest
from rest_framework import routers

#Medic_Back
from pacientes.views import PacienteView




routers = routers.DefaultRouter()

routers.register('pacientes', PacienteView)

urlpatterns = [
    path('', include(routers.urls)),
]
