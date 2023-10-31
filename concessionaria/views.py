from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa
from .models import Veiculo
from django.core.paginator import Paginator
# Create your views here.



def index(request):
    return HttpResponse("Olá mundo!")

def home(request):
     veiculos = Veiculo.objects.all()
     return render(request, 'homejm.html' ,  {'veiculos': veiculos})

def veiculos(request):

  veiculos = Veiculo.objects.all()

  marcas = Veiculo.objects.values_list('marca', flat=True).distinct()

  context = {
    'veiculos': veiculos,
    'marcas': marcas
  }

  paginator = Paginator(veiculos, 2)

  page = request.GET.get('page')

  veiculos_paginados = paginator.get_page(page)

  context['veiculos'] = veiculos_paginados

  return render(request, 'veiculos.html', context)

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

