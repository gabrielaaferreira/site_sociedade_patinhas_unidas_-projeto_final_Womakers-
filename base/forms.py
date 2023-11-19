from django import forms 
from base.models import Cadastro

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = ['nome', 'email', 'telefone', 'tipocasa', 'motivoadocao', 'historico']

class AnimalSearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False, label='Search Animals')