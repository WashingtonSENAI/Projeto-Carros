from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa

# Create your views here.
def home(request):
     return render(request, 'home.html')

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


def lista_teste(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'listar_teste.html', {'pessoas': pessoas})


# def listar_veiculos(request):
#     veiculos = Veiculo.objects.all()
#     return render(request, 'veiculos.html', {'veiculos': veiculos})

# def adicionar_veiculo(request):
#     if request.method == 'POST':
#         marca = request.POST['marca']
#         modelo = request.POST['modelo']
#         ano = request.POST['ano']
#         preco = request.POST['preco']
#         Veiculo.objects.create(marca=marca, modelo=modelo, ano=ano, preco=preco)
#         return redirect('listar_veiculos')
#     return render(request, 'adicionar_veiculo.html')

# def excluir_veiculo(request, veiculo_id):
#     veiculo = Veiculo.objects.get(pk=veiculo_id)
#     veiculo.delete()
#     return redirect('listar_veiculos')

