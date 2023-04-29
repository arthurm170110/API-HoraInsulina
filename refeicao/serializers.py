from rest_framework import serializers
from .models import Refeicao
from datetime import datetime, timedelta


class RefeicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Refeicao
        fields = '__all__'
        read_only_fields = ('hora_alarme',)

    def calculo_hora(self, data):
        
        hora_alarme = datetime.combine(datetime.today(), data['horario']) - timedelta(minutes=20)
        return hora_alarme.time()

    def create(self, validated_data):
        
        hora_alarme = self.calculo_hora(validated_data)
        return Refeicao.objects.create(hora_alarme=hora_alarme, **validated_data)
    
    def update(self, instance, validated_data):
        instance.nome = validated_data.get('nome', instance.nome)
        instance.horario = validated_data.get('horario', instance.horario)
        instance.alarme = validated_data.get('alarme', instance.alarme)
        instance.usuario = validated_data.get('usuario', instance.usuario)

        hora_alarme = datetime.combine(datetime.today(), instance.horario) - timedelta(minutes=20)
        hora_alarme = hora_alarme.time()

        instance.hora_alarme = validated_data.get('hora_alarme', hora_alarme)

        instance.save()
        return instance
