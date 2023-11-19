from django.shortcuts import render
from django.http import HttpResponse 
from base.forms import CadastroForm
from base.models import Cadastro, Animal
from django.shortcuts import get_object_or_404

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')

def faq(request):
    return render(request, 'faq.html')

def ficha(request):
    return render(request, 'ficha.html')

def ficha001(request):
    animal_instance = get_object_or_404(Animal, id_ficha=1)
    return render(request, 'fichas_animais/ficha001_Manu.html', {'animal': animal_instance})

def cadastro(request):
    sucesso = False
    mensagem = None

    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            sucesso = True
            mensagem = "Cadastro realizado com sucesso."
            # Pode adicionar redirecionamento ou outras lógicas aqui
        else:
            mensagem = "Erro no formulário. Por favor, corrija os erros e tente novamente."
    else:
        form = CadastroForm()

    contexto = {
        'form': form,
        'sucesso': sucesso,
        'mensagem': mensagem,
    }
    return render(request, 'cadastro.html', contexto)
    
