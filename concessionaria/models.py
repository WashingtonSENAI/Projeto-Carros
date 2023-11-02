from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.IntegerField()

    def __str__(self) -> str:
         return self.nome


class Veiculo(models.Model):
    
    marca = models.CharField(max_length=100, null= False)
    tipo = models.CharField(max_length = 100,  null= False)
    modelo = models.CharField(max_length=100, null= False)
    cor = models.CharField(max_length=100 ,null= False)
    estado = models.CharField(max_length=100, null= False)
    ano = models.IntegerField(null= False)
    preco = models.DecimalField(max_digits=10, decimal_places=2 , null= False)
    kmrodados =  models.DecimalField(max_digits=10, decimal_places=2, null= False)	
    forma_de_pagamento=  models.CharField(max_length=100, null= False)
    imagem = models.ImageField(upload_to='imagens/', null=False, blank=True)
    def __str__(self):
        return f" Marca: {self.marca} - Modelo: {self.modelo} - Cor: {self.cor} - Estado: {self.estado} - Ano: {self.ano} - Preço: {self.preco} - KM Rodados: {self.kmrodados} "


class Contato(models.Model):
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    def __str__(self):
       return f"{self.email}"




# class Veiculo(models.Model):
#     marca = models.CharField(max_length=100)
#     modelo = models.CharField(max_length=100)
#     ano = models.IntegerField()
#     preco = models.DecimalField(max_digits=10, decimal_places=2)
#     kmrodados =  models.DecimalField(max_digits=10, decimal_places=2)	
#     forma_de_pagamento=  models.CharField(max_length=100)

