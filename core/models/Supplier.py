from django.db import models
from core.models import BaseUser


class Supplier(BaseUser):
    fantasy_name = models.CharField('Razão Social', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=14, unique=True, blank=False, null=False)

    def __str__(self):
        return self.fantasy_name

    