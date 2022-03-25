from dataclasses import Field
from pyexpat import model
from rest_framework import serializers
from frexco.models  import Funcionario

class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Funcionario
        fields  = ['id', 'nome', 'nascimento']
