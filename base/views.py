from django.shortcuts import render,redirect
from django.http import HttpResponse 
from base.forms import CadastroForm, AnimalSearchForm
from base.models import Cadastro, Animal
from django.shortcuts import get_object_or_404, render
from django.db.models import Q

# Create your views here.
def inicio(request):
    animais = Animal.objects.all()
    return render(request, 'inicio.html', {'animais': animais})

def quem_somos(request):
    return render(request, 'quem_somos.html')

def futuras_atualizacoes(request):
    return render(request, 'futuras_atualizacoes.html')

def ficha(request):
    return render(request, 'ficha.html')

def animal_detail(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    return render(request, 'animal_detail.html', {'animal': animal})

def sua_view(request):
    animal_2 = Animal.objects.get(id_ficha=2)
    return render(request, 'inicio.html', {'animal_2': animal_2})

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirecionar para a página de sucesso após o cadastro
            return HttpResponse('Cadastro realizado com sucesso.')

    # Se o método não for POST ou o formulário não for válido, renderizar o formulário
    form = CadastroForm()
    contexto = {'form': form}
    return render(request, 'cadastro.html', contexto)

    
def animal_search(request):
    form = AnimalSearchForm(request.GET)
    animals = Animal.objects.all()

    if form.is_valid():
        query = form.cleaned_data['query']
        if query:
            animals = animals.filter(
                Q(nome__icontains=query) | 
                Q(especie__icontains=query) |
                Q(raca__icontains=query) )

    context = {'animals': animals, 'form': form}
    return render(request, 'animal_search.html', context)