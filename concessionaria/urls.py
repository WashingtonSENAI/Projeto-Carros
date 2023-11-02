from django.urls import path
from . import views

urlpatterns = [
    
    path('home/', views.home, name="home"),
    path('sobrenos/', views.sobrenos, name="sobrenos"),
    path('teste/', views.teste, name="veiculos"),
    path('veiculos/', views.veiculos, name='veiculos'),

]
