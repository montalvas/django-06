from django.db import models


class Base(models.Model):
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    activated = models.BooleanField(default=True)
    
    class Meta:
        abstract = True

class Field(Base):
    name = models.CharField('Nome', max_length=50)
    description = models.CharField('Descrição', max_length=100)
    
    class Meta:
        verbose_name = 'Campo'
        verbose_name_plural = 'Campos'
    
    def __str__(self):
        return self.name
    
class Activity(Base):
    number = models.IntegerField('Número')
    description = models.CharField('Descrição', max_length=100)
    points = models.DecimalField('Pontos', decimal_places=1, max_digits=4)
    details = models.CharField('Detalhes', max_length=100)
    
    field = models.ForeignKey(Field, on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'
        
    def __str__(self):
        return f'{self.number} - {self.description} ({self.field.name})'
