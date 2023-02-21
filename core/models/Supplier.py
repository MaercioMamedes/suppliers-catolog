from django.db import models
from django.contrib.auth.models import User


class Supplier(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    cnpj = models.CharField('CNPJ', max_length=14, unique=True, blank=False, null=False)
    likes = models.IntegerField('Likes', default=0)

    def delete(self, *args, **kwargs):
        self.user.delete()
        return super(self.__class__, self).delete(*args, **kwargs)
    