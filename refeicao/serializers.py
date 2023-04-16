from rest_framework import serializers
from .models import Refeicao


class RefeicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refeicao
        fields = '__all__'
