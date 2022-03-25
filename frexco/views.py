# Django e outras aplicações
from rest_framework             import viewsets, status
from rest_framework.response    import Response
from rest_framework.decorators  import api_view
from django.shortcuts           import redirect, render
from django.contrib             import messages
# Aplicações Nossas
from frexco.models              import Funcionario
from frexco.serializer          import FuncionarioSerializer
from frexco.forms               import FuncionarioForm


def Home(request):
    funcionarios = Funcionario.objects.all()

    context = {
        'funcionarios': funcionarios,
    }

    return render(request, 'home.html', context)

@api_view(['GET'])
def ConsultarUsuarios(request):
    funcionarios = Funcionario.objects.all()
    list_func = []

    if funcionarios.exists():
        for v in funcionarios:
            list_func.append({
                'nome': v.nome,
                'nascimento': v.nascimento,
            })
        return Response(list_func, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Nenhum funcionário encontrado.'}, status=status.HTTP_404_FORBIDDEN)

def AddFuncionarios(request, template_name= 'AddFuncionario.html'):
    try:
        form = FuncionarioForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                funcionario = form.save(commit=False)
                funcionario.save()

                messages.success(request, "Funcionário criado com sucesso")
                
                return redirect('home')
    except Exception:
        messages.error(request, "Erro ao cadastrar Funcionário!")
    return render(request, template_name, {'form': form})

# Função para gerar e exibir todos os meus dados de Funcionário
class FuncionarioViewSet(viewsets.ModelViewSet):
    # Trazer todos os meus funcionários
    queryset = Funcionario.objects.all()
    # Quem vai ser responsável por trazer todos eles
    serializer_class = FuncionarioSerializer
