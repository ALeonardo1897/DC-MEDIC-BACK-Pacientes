from rest_framework import viewsets

from pacientes.models import Paciente
from pacientes.serializers import PacienteSerializer
from rest_framework.permissions import IsAuthenticated

class PacienteView(viewsets.ModelViewSet):

    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = (IsAuthenticated,)
