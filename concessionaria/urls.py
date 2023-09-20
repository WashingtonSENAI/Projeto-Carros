from django.urls import path
from . import views

urlpatterns = [
    
    path('home/', views.home, name="home"),
    path('sobrenos/', views.sobrenos, name="sobrenos"),
    path('teste/', views.teste, name="teste"),
    # path('veiculos/', views.listar_veiculos, name='listar_veiculos'),
    # path('veiculos_admin/adicionar/', views.adicionar_veiculo, name='adicionar_veiculo'),
    # path('veiculos_admin/excluir/<int:veiculo_id>/', views.excluir_veiculo, name='excluir_veiculo'),

]
