# Generated by Django 5.0.6 on 2024-06-06 20:39

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=255)),
                ('ano', models.CharField(max_length=4)),
                ('placa', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(code='invalid_placa', message='A placa deve ter o formato AAA-9999.', regex='^[A-Z]{3}[0-9]{4}$')])),
                ('chassi', models.CharField(max_length=17)),
                ('tipo', models.IntegerField(choices=[(1, 'Carro'), (2, 'Caminhao'), (3, 'Picape')])),
            ],
        ),
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razaoSocial', models.CharField(max_length=255)),
                ('nomeFantasia', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('cnpj', models.CharField(max_length=18)),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veiculo.veiculo')),
            ],
        ),
    ]
