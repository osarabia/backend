from django.contrib.auth.models import User, Group
from rest_framework import serializers
from spa_gastos.gastos.models import Gastos



class GastosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gastos
        fields = ('id', 'fecha', 'concepto', 'cantidad',)
