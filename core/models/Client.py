from core.models import BaseUser
from django.db import models


class Client(BaseUser):
    fullname = models.CharField('Nome Completo', max_length=100)
    cpf = models.CharField('CPF', max_length=11, unique=True, blank=False, null=False)

    def __str__(self):
        return self.user.first_name
