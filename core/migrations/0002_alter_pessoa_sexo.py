# Generated by Django 5.0.6 on 2024-06-07 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='sexo',
            field=models.IntegerField(choices=[(1, 'Masculino'), (2, 'Feminino')]),
        ),
    ]
