from django.db import models


class Category(models.Model):
    name = models.CharField('Nome da Categoria', max_length=20, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name