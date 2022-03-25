from django.db   import models
# Realizando o import pra nossa função de senha
import random 
import uuid

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

# Local onde declaramos nossas models DB
class Funcionario(models.Model):
    nome        = models.CharField(max_length=30)
    senha       = models.CharField(max_length=30, default=uuid.uuid4().hex, blank=True, null=True)
    nascimento  = models.DateField()

    def __str__(self):
        return self.nome   
