from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    full_name = models.CharField('Nome Completo', max_length=50, null=True)
    cpf = models.CharField('CPF', max_length=14, null=True)
    phone = models.CharField('Telefone', max_length=16, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Usuário')
    
    def __str__(self):
        return f'{self.user}'
