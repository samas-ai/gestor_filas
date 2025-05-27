from django.db import models
from django.contrib.auth.models import User

class Paciente(models.Model):
    # ... (seu modelo de Paciente aqui)
    nome_completo = models.CharField(max_length=255, verbose_name='Nome Completo')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    idade = models.IntegerField(blank=True, null=True, verbose_name='Idade')
    nome_mae = models.CharField(max_length=255, verbose_name='Nome da Mãe')
    carteira_sus = models.CharField(max_length=20, unique=True, verbose_name='Carteira do SUS')
    plano_saude = models.CharField(max_length=100, blank=True, null=True, verbose_name='Plano de Saúde')
    queixa_principal = models.TextField(blank=True, null=True, verbose_name='Queixa Principal')
    inicio_doenca = models.TextField(blank=True, null=True, verbose_name='Quando a doença começou')
    localizacao_dor = models.CharField(max_length=255, blank=True, null=True, verbose_name='Localização da Dor')
    caracteristicas_dor = models.TextField(blank=True, null=True, verbose_name='Características da Dor')
    evolucao_quadro = models.TextField(blank=True, null=True, verbose_name='Evolução do quadro')
    alergias = models.TextField(blank=True, null=True, verbose_name='Alergias')
    doencas_pre_existentes = models.TextField(blank=True, null=True, verbose_name='Doenças Pre-existentes')

    def __str__(self):
        return self.nome_completo

class Medico(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    especialidade = models.CharField(max_length=100, verbose_name='Especialidade')
    crm = models.CharField(max_length=20, unique=True, verbose_name='CRM')
    telefone = models.CharField(max_length=20, blank=True, null=True, verbose_name='Telefone')
    email = models.EmailField(blank=True, null=True, verbose_name='Email')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} ({self.especialidade})'

# Podemos não precisar de um modelo de Atendente separado agora,
# pois podemos usar o próprio modelo User do Django para eles.