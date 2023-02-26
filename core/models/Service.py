from django.db import models
from core.models import Supplier
from core.models import Category


class Service(models.Model):
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField('título', max_length=50, null=False, blank=False)
    description = models.TextField('Descrição')
    price = models.DecimalField('Preço', max_digits=10, decimal_places=2)
    image = models.ImageField('Foto', upload_to='pictures/service')
    published = models.BooleanField('Publicado', default=False)
    created_in = models.DateTimeField('Criado em:  ', auto_now_add=True)
    modified_in = models.DateTimeField('modificado em: ', auto_now=True)

    def __str__(self):
        return self.title
