from django.contrib import admin
from .models import Perfil, Experiencia, Curso

# Esto permite que aparezcan en el panel /admin
admin.site.register(Perfil)
admin.site.register(Experiencia)
admin.site.register(Curso)