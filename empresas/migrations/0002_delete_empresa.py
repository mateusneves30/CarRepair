# Generated by Django 5.0.6 on 2024-06-17 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
        ('servicos', '0004_remove_servico_empresa_alter_ordemservico_status'),
        ('usuarios', '0002_remove_funcionario_empresa'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Empresa',
        ),
    ]
