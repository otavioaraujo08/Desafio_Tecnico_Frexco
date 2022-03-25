# Funções Django
from django.contrib import admin
from django.urls    import path, include
# Funções Rest Framework
from rest_framework import routers
# Funções da Nossa Aplicação Principal
from frexco.views   import Home, ConsultarUsuarios, AddFuncionarios, FuncionarioViewSet

# Definindo a rota principal
router = routers.DefaultRouter()
# Definindo nossa rota principal como FuncionarioViewSet
router.register(r'Funcionarios', FuncionarioViewSet)

urlpatterns = [
    # Nossa Página Principal
    path('', Home, name="home"),

    # Página de List Funcionarios
    path('List_Funcionarios', ConsultarUsuarios),

    # Página Responsável por Adicionar Funcionários
    path('Add_Funcionarios', AddFuncionarios),

    # Página de Admin
    path('admin/', admin.site.urls),
    
    # Página de Funcionário do Rest
    path('Funcionarios/', include(router.urls)),
]
