
# Django
from django.db import models
#Django Validators
from django.core.validators import RegexValidator
# Medic_Back
from medic_back_pacientes.utils.models import MedicBaseClass

class Paciente(MedicBaseClass):

    nombres = models.CharField(
        max_length=60,
    )

    apellidos = models.CharField(
        max_length=60,
    )

    dni_regex = RegexValidator(
        regex = r'\d{8}',
        message="El campo dni debe contener 8 dígitos"
    )
    dni = models.CharField( max_length=8, unique=True, validators=[dni_regex] )

    direccion = models.CharField(
        max_length=60
    )

    telefono_regex = RegexValidator(
        regex = r'\d{9}',
        message="El campo teléfono debe contener 9 dígitos"
    )
    telefono = models.CharField( max_length=20, null=True, validators=[telefono_regex])

    email = models.EmailField(
        unique=True
    )

    class Meta:
        db_table = "pacientes"