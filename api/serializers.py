from rest_framework import serializers
from .models import *


class EstadoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ('sigla', 'numeroCasos', 'recuperados', 'vacinados', 'numeroMortos')