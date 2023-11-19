from django.db import models

# Create your models here.
class Cadastro(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    telefone = models.CharField(max_length=12)
    tipocasa = models.CharField(max_length=4)
    motivoadocao = models.CharField(max_length=50)
    historico = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.nome} [{self.email}]'
    class Meta:
        verbose_name = 'Formulário de adoção'
        verbose_name_plural = 'Formulários de adoção'
        ordering = ['-data']


class Animal(models.Model):
    id_ficha = models.IntegerField(null=True, blank=True)
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    idade = models.IntegerField(null=True, blank=True)
    raca = models.CharField(max_length=100)
    historico_saude = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name= 'Ficha Animal'
        verbose_name_plural = 'Fichas Animais'
        ordering = ['nome']


class Registro(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    data = models.DateField()
    descricao = models.TextField()

    def __str__(self):
        return f"{self.animal.nome} - {self.data}"
    class Meta:
        verbose_name= 'Registro'
        verbose_name_plural = 'Registros'


class HistoricoAdocao(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    nome_tutor = models.CharField(max_length=100)
    data_adoção = models.DateField()

    def __str__(self):
        return f"{self.animal.nome} - {self.nome_tutor}"
    class Meta:
        verbose_name= 'Historido de Adoção'
        verbose_name_plural = 'Históricos de Adoção'


class Cuidador(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    responsável_por= models.CharField(max_length=200)

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name= 'Cuidador'
        verbose_name_plural = 'Cuidadores'
    
    
class Voluntario(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name= 'Voluntário'
        verbose_name_plural = 'Voluntários'