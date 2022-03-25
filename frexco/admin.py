from django.contrib import admin
from frexco.models  import Funcionario 

class Funcionarios(admin.ModelAdmin):
    # Itens que vou exibir
    list_display       = ('id', 'nome', 'nascimento', 'senha')
    # Itens que podemos exibir
    list_display_links = ('id', 'nome')
    # Itens que podem ser pesquisados
    search_fields      = ('nome',)

admin.site.register(Funcionario, Funcionarios)
