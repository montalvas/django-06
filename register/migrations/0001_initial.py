# Generated by Django 2.2.12 on 2022-02-23 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Criado')),
                ('updated', models.DateField(auto_now=True, verbose_name='Atualizado')),
                ('activated', models.BooleanField(default=True, verbose_name='Ativo')),
                ('name', models.CharField(max_length=50, verbose_name='Nome')),
                ('description', models.CharField(max_length=100, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Campo',
                'verbose_name_plural': 'Campos',
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Criado')),
                ('updated', models.DateField(auto_now=True, verbose_name='Atualizado')),
                ('activated', models.BooleanField(default=True, verbose_name='Ativo')),
                ('number', models.IntegerField(verbose_name='Número')),
                ('description', models.CharField(max_length=100, verbose_name='Descrição')),
                ('points', models.DecimalField(decimal_places=1, max_digits=4, verbose_name='Pontos')),
                ('details', models.CharField(max_length=100, verbose_name='Detalhes')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='info.Field')),
            ],
            options={
                'verbose_name': 'Atividade',
                'verbose_name_plural': 'Atividades',
            },
        ),
    ]
