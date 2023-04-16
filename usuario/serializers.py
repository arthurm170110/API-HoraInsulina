from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Usuario
from validacao.validators import *


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self):
        conta = Usuario(
            email=self.validated_data['email'], 
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name']
        )

        password = self.validated_data['password']
        
        conta.set_password(password)
        conta.save()

        return conta
    
    def update(self, instance, validated_data):



        instance.email = validated_data.get('email', instance.email)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        password = validated_data.get('password', instance.password)

       
        instance.set_password(password)


        instance.save()
        
        return instance 

        

    def validate(self, data):
        sem_espaco(data['username'])
        nome_valido(data['first_name'])
        sobrenome_valido(data['last_name'])
        senha_valida(data['password'])

        return data
