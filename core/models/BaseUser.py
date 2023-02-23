from django.db import models
from django.contrib.auth.models import User


class BaseUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField('telefone', max_length=11, default='')
    district = models.CharField('Bairro', max_length=50, default='')
    public_place = models.CharField('Logradouro', max_length=150, default='')
    uf = models.CharField('UF', max_length=2, default='')
    city = models.CharField('Cidade', max_length=50, default='')
    cep = models.CharField('CEP', max_length=9, default='')
    property_number = models.CharField('Número', max_length=5, default=0)
    likes = models.IntegerField('Likes', default=0)

    class Meta:
        abstract = True


