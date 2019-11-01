from django.contrib import admin
from .models import *

@admin.register(Publicacao)
class PublicacaoAdmin(admin.ModelAdmin):
    pass

@admin.register(Colaborador)
class ColaboradorAdmin(admin.ModelAdmin):
    pass