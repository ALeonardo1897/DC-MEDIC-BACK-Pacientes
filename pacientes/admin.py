#Django
from django.contrib import admin

#Medic_Back
from pacientes.models import Paciente

class PacienteAdmin(admin.ModelAdmin):

    list_display = ('nombres','apellidos','email','direccion')
    list_filter = ('created','modified')

admin.site.register(Paciente,PacienteAdmin)