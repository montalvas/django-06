from django.db import models
from django.contrib.auth.models import User


class Base(models.Model):
    created = models.DateField('Criado', auto_now_add=True)
    updated = models.DateField('Atualizado', auto_now=True)
    activated = models.BooleanField('Ativo', default=True)
    
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
    description = models.TextField('Descrição')
    points = models.DecimalField('Pontos', decimal_places=1, max_digits=4)
    details = models.CharField('Detalhes', max_length=100, null=True, blank=True)
    
    field = models.ForeignKey(Field, on_delete=models.PROTECT, verbose_name='Campo')
    
    class Meta:
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'
        
    def __str__(self):
        return f'{self.number} - {self.description} ({self.field.name})'

class State(models.Model):
    name = models.CharField('Nome', max_length=50)
    uf = models.CharField('UF', max_length=2)
    
    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
    
    def __str__(self):
        return f'{self.uf}'

class City(models.Model):
    name = models.CharField('Nome', max_length=50)
    state = models.ForeignKey(State, on_delete=models.PROTECT, verbose_name='Estado')
    
    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
    
    def __str__(self):
        return f'{self.name}'
    
class Campus(models.Model):
    name = models.CharField('Nome', max_length=100)
    city = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name='Cidade')
    address = models.CharField('Endereço', max_length=150)
    phone = models.CharField('Telefone', max_length=15)
    
    def __str__(self) -> str:
        return f'{self.name}'
    
class Official(models.Model):
    full_name = models.CharField('Nome Completo', max_length=100)
    siape = models.CharField('SIAPE', max_length=10)
    cpf = models.CharField('CPF', max_length=14)
    campus = models.ForeignKey(Campus, on_delete=models.PROTECT, verbose_name='Campus')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuário')
    
    class Meta:
        verbose_name = 'Servidor'
        verbose_name_plural = 'Servidores'
        
    def __str__(self):
        return f'{self.full_name} ({self.siape})'
    
class Status(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.CharField('Descrição', max_length=150)
    
    def __str__(self):
        return f'{self.name} ({self.description})'

class Situation(models.Model):
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name='Situação')
    created = models.DateField('Movimentado em', auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Movimentado por')
    details = models.CharField(max_length=255, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Situação'
        verbose_name_plural = 'Situações'
    
    def __str__(self):
        return f'{self.status} em {self.created} por {self.owner}'

class Grade(models.Model):
    name = models.CharField('Nome', max_length=50)
    level = models.IntegerField('Nível')
    description = models.CharField('Descrição', max_length=150, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Classe'
        verbose_name_plural = 'Classes'
    
    def __str__(self):
        return f'{self.name} nível {self.level}'
    
class Progression(models.Model):
    grade = models.ForeignKey(Grade, on_delete=models.PROTECT, verbose_name='Classe')
    initial_date = models.DateField('Data inicial')
    final_date = models.DateField('Data final')
    observation = models.CharField('Observação', max_length=255)
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Usuário')
    
    class Meta:
        verbose_name = 'Progressão'
        verbose_name_plural = 'Progressões'
    
    def __str__(self):
        return f'{self.user} -> {self.grade} | {self.initial_date} a {self.final_date}'
    
class Receipt(models.Model):
    progression = models.ForeignKey(Progression, on_delete=models.PROTECT, verbose_name='Progressão')
    activity = models.ForeignKey(Activity, on_delete=models.PROTECT, verbose_name='Atividade')
    quantity = models.DecimalField('Quantidade', max_digits=5, decimal_places=2)
    initial_date = models.DateField('Data inicial')
    final_date = models.DateField('Data final', null=True, blank=True, help_text='Informar apenas se o comprovante for relativo a um período.')
    file = models.FileField(upload_to='pdf/')
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = 'Comprovante'
        verbose_name_plural = 'Comprovantes'
    
    def __str__(self):
        return f'[{self.pk}] {self.user} - {self.progression}/{self.activity}'
    
class Validation(models.Model):
    receipt = models.ForeignKey(Receipt, on_delete=models.PROTECT, verbose_name='Comprovante')
    validated_in = models.DateTimeField('Validado em', auto_now_add=True)
    validated_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Validado por')
    quantity = models.DecimalField('Quantidade', max_digits=5, decimal_places=2)
    justification = models.TextField('Justificativa', max_length=255)
    
    class Meta:
        verbose_name = 'Validação'
        verbose_name_plural = 'Validações'
        
    def __str__(self):
        return f'[{self.receipt.pk}] Pontuação: {self.quantity}/{self.receipt.quantity} por {self.validated_by}'