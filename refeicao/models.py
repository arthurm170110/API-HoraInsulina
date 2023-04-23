from django.db import models
from usuario.models import Usuario


class Refeicao(models.Model):

    nome = models.CharField(max_length=45)
    horario = models.TimeField()
    alarme = models.BooleanField(default=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome
