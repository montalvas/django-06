from django.db import models


class Base(models.Model):
    created = models.DateField('Criado', auto_now_add=True)
    updated = models.DateField('Atualizado', auto_now=True)
    activated = models.BooleanField('Ativo', default=True)
    
    class Meta:
        abstract = True

class State(Base):
    name = models.CharField('Estado', max_length=50)
    uf = models.CharField('UF', max_length=2)
    
    def __str__(self):
        return self.uf

class City(Base):
    name = models.CharField('Cidade', max_length=100)
    state = models.ForeignKey(State, on_delete=models.PROTECT, verbose_name='Estado')
    
    def __str__(self):
        return self.name
    
class Campus(Base):
    name = models.CharField('Nome', max_length=100)
    city = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name='Cidade')
    address = models.CharField('Endereço', max_length=150)
    phone = models.CharField('Telefone', max_length=15)
    
    def __str__(self):
        return self.name
    

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
    
    field = models.ForeignKey(Field, on_delete=models.PROTECT, verbose_name='Campo')
    
    class Meta:
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'
        
    def __str__(self):
        return f'{self.number} - {self.description} ({self.field.name})'
