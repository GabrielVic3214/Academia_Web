from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    idade = models.IntegerField()
    Email = models.EmailField()
    tel1 = models.IntegerField()
    tel2 = models.IntegerField()
    cpf = models.IntegerField()
    cep = models.IntegerField()
    Bairro = models.CharField(max_length=255, null=True, blank=True)
    Estado = models.CharField(max_length=255, null=True, blank=True)
    Cidade = models.CharField(max_length=255, null=True, blank=True)
    Rua = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'O nome do cliente é {self.nome} e seu cpf é {self.cpf}'
    
class Parceiro(models.Model):
    NomEmp = models.CharField(max_length=255)
    NomFantasia = models.CharField(max_length=255)
    cnpj = models.IntegerField()
    telefone = models.IntegerField()
    email = models.EmailField()
    cep = models.IntegerField()
    estado = models.CharField(max_length=255)
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)

    def __str__(self):
        return f'Empresa {self.NomEmp} com cnpj {self.cnpj} é parceiro do nosso site'
    
class Modalidade(models.Model):
    NomMod = models.CharField(max_length=255)
    DescMod = models.CharField(max_length=400)
    QuantAlu = models.IntegerField()

    def __str__(self):
        return f'Modalidade {self.NomMod} cadastrada com sucesso'
    

class Fichas(models.Model):
    Nome = models.CharField(max_length=128)
    MasCor = models.IntegerField()
    idade = models.IntegerField()
    Altura = models.IntegerField()
    peso = models.IntegerField()
    observacao = models.TextField()

    def __str__(self):
        return f'Ficha para o {self.Nome}, cadastrada com sucesso!'
    