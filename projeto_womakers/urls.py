from django.contrib import admin
from django.urls import path
from base.views import inicio, cadastro, quem_somos, animal_search, animal_detail
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio),
    path('cadastro/', cadastro, name='cadastro'),
    path('quem_somos/', quem_somos),
    path('animal/search/', animal_search, name='animal_search'),
    path('animal/<int:animal_id>/', animal_detail, name='animal_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)