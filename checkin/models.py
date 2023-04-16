from django.db import models
from usuario.models import Usuario


class Checkin(models.Model):

    glicose = models.FloatField()
    data = models.DateField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
