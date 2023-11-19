from django import forms 
from base.models import Cadastro

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = ['nome', 'email', 'telefone', 'tipocasa', 'motivoadocao', 'historico']

class AnimalSearchForm(forms.Form):
    query = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'class': 'form-control me-2', 'type': 'search', 'placeholder': 'Search', 'aria-label': 'Search'})
    )