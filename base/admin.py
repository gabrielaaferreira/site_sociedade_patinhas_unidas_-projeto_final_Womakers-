from django.contrib import admin
from base.models import Cadastro, Animal, Registro, HistoricoAdocao, Cuidador, Voluntario
# Register your models here.

admin.site.register(Cadastro)
admin.site.register(Animal)
admin.site.register(Registro)
admin.site.register(HistoricoAdocao)
admin.site.register(Cuidador)
admin.site.register(Voluntario)