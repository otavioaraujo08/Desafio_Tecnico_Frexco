from asyncio.windows_events import NULL
from multiprocessing.sharedctypes import Value
from django         import forms
from frexco.models  import Funcionario
from datetime       import datetime
import random 

def GerarSenha():
    min = 'abcdefghijklmnopqrstuvwxyz'
    max = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num = '0123456789'
    sybs = '[]{}()*#;/,-_%'

    qnt = 5
    qntInt = int(qnt)
    length = qntInt

    #fazendo senha com todos
    all = min + max + num + sybs
    passwordAll = "".join(random.sample(all,length))

    return passwordAll

def process_data():
    return datetime.now().date()

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'nascimento', 'senha']
        widgets = {
            'nome':       forms.TextInput(),
            'nascimento': forms.DateInput(attrs={'class': 'form-control',  'max': process_data()}),
            'senha':      forms.PasswordInput(attrs={'value': GerarSenha()})
        }
