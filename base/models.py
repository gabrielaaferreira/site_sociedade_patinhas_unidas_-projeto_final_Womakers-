from django.db import models

# Create your models here.
class Cadastro(models.Model):
    nome = models.CharField(max_length=50, default='Valor Padrão')
    email = models.EmailField(max_length=75, default='Valor Padrão')
    telefone = models.CharField(max_length=50, default='Valor Padrão')
    tipocasa = models.CharField(max_length=50, default='Valor Padrão')
    motivoadocao = models.CharField(max_length=50, default='Valor Padrão')
    historico = models.CharField(max_length=50, default='Valor Padrão')
    data = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.nome} [{self.email}]'
    class Meta:
        verbose_name = 'Formulário de contato'
        verbose_name_plural = 'Formulários de contatos'
        ordering = ['-data']
  