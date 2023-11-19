from django import forms
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from base.models import Cadastro, Animal, Registro, HistoricoAdocao, Cuidador, Voluntario
# Register your models here.

class AnimalAdminForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'

class AnimalAdmin(admin.ModelAdmin):
    form = AnimalAdminForm
    list_display = ['id_ficha', 'nome', 'especie', 'idade', 'raca', 'historico_saude', 'display_foto']
    readonly_fields = ['display_foto']

    def display_foto(self, obj):
        if obj.foto:
            return format_html('<img src="{}" width="100" height="100" />', obj.foto.url)
        else:
            return 'No Image'

    display_foto.short_description = 'Foto'
    
    def ficha_link(self, obj):
        return format_html('<a href="{}">Ver Ficha</a>', reverse('ficha_animal', args=[obj.pk]))

    ficha_link.short_description = 'Ficha'

admin.site.register(Animal, AnimalAdmin)
admin.site.register(Cadastro)
admin.site.register(Registro)
admin.site.register(HistoricoAdocao)
admin.site.register(Cuidador)
admin.site.register(Voluntario)