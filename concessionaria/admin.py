from django.contrib import admin
from .models import Pessoa
from .models import Veiculo
from .models import Contato
from django.contrib.admin import AdminSite


class CustomAdminSite(AdminSite):
    site_title = 'GM Veículos'
    site_header = 'Painel de Administração da GM Veículos'
    index_title = 'Bem-vindo ao Painel de Administração da GM Veículos'

# Crie uma instância do site de administração personalizado
custom_admin_site = CustomAdminSite(name='custom_admin')



admin.site = custom_admin_site
admin.site.register(Veiculo)
admin.site.register(Contato)

## usuario : washington
## senha : 123