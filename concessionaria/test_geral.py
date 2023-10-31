from django.test import TestCase, Client
from .models import Veiculo
from django.urls import path, include
from . import views
from .views import home
from .views import veiculos
from.models import Pessoa


urlpatterns = [
  path('teste/', views.teste),
  path('veiculos/', views.veiculos),

]

class UrlTests(TestCase):


    def test_home_url(self):
        response = home(self.client.get('/home/'))
        self.assertEqual(response.status_code, 200)
        
    def test_veiculos_url(self):
       response = veiculos(self.client.get('/veiculos/'))
       self.assertEqual(response.status_code, 200)
        
        
class VeiculoTestCase(TestCase):
    def setUp(self):
        Veiculo.objects.create(
            marca='Ford',
            tipo='Carro',
            modelo='Ka',
            cor='Branco',
            estado='Novo',
            ano=2020, 
            preco=35000,
            kmrodados=0,
            forma_de_pagamento='Vista'
        )
        
    def test_veiculo_str(self):
         veiculo = Veiculo.objects.get(modelo='Ka')  
         parts = str(veiculo).split('-')
         km = float(parts[-1])

         self.assertEqual(km, 0.00)
        
    def test_veiculo_fields(self):
        veiculo = Veiculo.objects.get(modelo='Ka')
        self.assertEqual(veiculo.marca, 'Ford')
        self.assertEqual(veiculo.tipo, 'Carro')
        self.assertEqual(veiculo.modelo, 'Ka')


class TestViewTestCase(TestCase):

  def setUp(self):
    self.client = Client()

  def test_get_request(self):
    response = self.client.get('/teste/')
    
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.context['nome'], 'Jonas')  
    
  def test_post_request(self):

        response = self.client.post('/teste/', {
            'nome': 'Ana', 
            'idade': 25
        })

        pessoa = Pessoa.objects.get(nome='Ana')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(pessoa.nome, 'Ana')
        self.assertEqual(int(pessoa.idade), 25)
        
        
  def test_post_without_data(self):

            response = self.client.post('/teste/')

            self.assertEqual(response.status_code, 400)
            
            
  def test_duplicate_name(self):

    Pessoa.objects.create(nome='Maria', idade=30)

    response = self.client.post('/teste/', {
        'nome': 'Maria',
        'idade': 25  
    })

    self.assertEqual(response.status_code, 400)