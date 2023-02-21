from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('título', max_length=50)
    content = models.TextField('Conteúdo')
    created_in = models.DateTimeField('enviado em: ', auto_created=True)
