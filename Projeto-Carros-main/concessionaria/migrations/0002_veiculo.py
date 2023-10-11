# Generated by Django 4.2.6 on 2023-10-11 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concessionaria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('cor', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('ano', models.IntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('kmrodados', models.DecimalField(decimal_places=2, max_digits=10)),
                ('forma_de_pagamento', models.CharField(max_length=100)),
            ],
        ),
    ]
