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

def animal_detail(request, animal_id):
    animal = get_object_or_404(Animal, id=animal_id)
    return render(request, 'animal_detail.html', {'animal': animal})

def cadastro(request):
    cadastro_success = False
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            cadastro_success = True

    form = CadastroForm()
    contexto = {'form': form, 'cadastro_success': cadastro_success}
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