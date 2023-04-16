from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


def sem_espaco(user):
    if ' ' in user:
            raise serializers.ValidationError({'username':'Este campo nao pode possuir espacos'})
    return user


def nome_valido(nome):
    if not all(caractere.isalpha() or caractere.isspace() for caractere in nome):
        raise serializers.ValidationError({'first_name':'Este campo so pode possuir caracteres alfabeticos'})
    return nome


def sobrenome_valido(sobrenome):
    if not all(caractere.isalpha() or caractere.isspace() for caractere in sobrenome):
        raise serializers.ValidationError({'last_name':'Este campo so pode possuir caracteres alfabeticos'})
    return sobrenome


def senha_valida(senha):
    try:
        validate_password(senha)
    except ValidationError as erros:
        raise serializers.ValidationError({'password': erros.messages})
    return senha
