from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Pessoa
from .models import Veiculo
from django.core.paginator import Paginator
import urllib.parse
from django.urls import reverse
from .forms import ContatoForm
from django.contrib import messages
# Create your views here.



def index(request):
    return HttpResponse("Olá mundo!")

def home(request):
    
     veiculos = Veiculo.objects.all()
    
     if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            form.clean()
            messages.success(request, "Enviado com sucesso")
            print("ganhamos")
           
        else:
            messages.error(request, "Falha no envio, informações com falhas ou incompletas.")
            print("perdemos")
     else:
         form = ContatoForm()
     context = {
    'veiculos': veiculos,
    'form': form

     }
     
     paginator = Paginator(veiculos, 3)

     page = request.GET.get('page')

     veiculos_paginados = paginator.get_page(page)
     
    
     context['veiculos'] = veiculos_paginados
  
     
     return render(request, 'homejm.html' ,  context )

def veiculos(request):

  veiculos = Veiculo.objects.all()

  marcas = Veiculo.objects.values_list('marca', flat=True).distinct()
  tipos = Veiculo.objects.values_list('tipo', flat=True).distinct()
  modelos = Veiculo.objects.values_list('modelo', flat=True).distinct()
  anos = Veiculo.objects.values_list('ano', flat=True).distinct()
  estados = Veiculo.objects.values_list('estado', flat=True).distinct()
  
  marca = request.GET.get('marca')
  tipo = request.GET.get('tipo') 
  modelo = request.GET.get('modelo')
  ano = request.GET.get('ano')  
  estado = request.GET.get('estado') 
  
  if 'limpar' in request.POST:

      marca = None
      ano = None 
      modelo = None
      tipo = None
      

  veiculos = Veiculo.objects.all()
  ano = int(ano) if ano else ano
  
  try:
     if ano:
      veiculos = veiculos.filter(ano=ano)
  except Exception as e: 
      print(e)
  if marca:
      veiculos = veiculos.filter(marca=marca)
      

  if tipo:  
      veiculos = veiculos.filter(tipo=tipo)

  if modelo:
      veiculos = veiculos.filter(modelo=modelo)  

  if ano:
      veiculos = veiculos.filter(ano=ano)
      
  if estado:
      veiculos = veiculos.filter(estado=estado)


    
  context = {
    'veiculos': veiculos,
    'marcas': marcas,
    'tipo' : tipos,
    'modelo' : modelos,
    'ano' : anos,
    'estado' : estados
  }


  paginator = Paginator(veiculos, 6)

  page = request.GET.get('page')

  veiculos_paginados = paginator.get_page(page)

  context['veiculos'] = veiculos_paginados
  
  base_url = request.path_info
  query_params = request.GET.copy()
  if page:
        query_params['page'] = page
  page_url = f"{base_url}?{query_params.urlencode()}"
  context['page_url'] = page_url
  


  return render(request, 'veiculos.html', context )

def sobrenos(request):
      return render(request, 'sobrenos.html')

def teste(request):
      if request.method == "GET":
            nome='Jonas'
            return render(request, 'teste.html', {'nome': nome})
      elif request.method == "POST":
            nome = request.POST.get('nome')
            idade = request.POST.get('idade')
            
            pessoa = Pessoa(nome=nome, idade=idade)
            
            pessoa.save()
            
            ##LISTAR AS PESSOAS
            
            ##pessoas = Pessoa.objects.all()
            
            pessoas = Pessoa.objects.filter(nome=nome)
            
            return HttpResponse(pessoas)

