from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):

    username = models.CharField(max_length=25, unique=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True, error_messages={'unique': "O email informado ja existe."})

    USERNAME_FIELD = 'username'


    def __str__(self) -> str:
        return self.username
