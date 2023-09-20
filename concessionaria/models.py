from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()

    def __str__(self) -> str:
         return self.nome


class Veiculo(models.Model):
    
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    cor = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    ano = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    kmrodados =  models.DecimalField(max_digits=10, decimal_places=2)	
    forma_de_pagamento=  models.CharField(max_length=100)
    def __str__(self) -> str:
         return self.marca , self.modelo      







# class Veiculo(models.Model):
#     marca = models.CharField(max_length=100)
#     modelo = models.CharField(max_length=100)
#     ano = models.IntegerField()
#     preco = models.DecimalField(max_digits=10, decimal_places=2)
#     kmrodados =  models.DecimalField(max_digits=10, decimal_places=2)	
#     forma_de_pagamento=  models.CharField(max_length=100)

