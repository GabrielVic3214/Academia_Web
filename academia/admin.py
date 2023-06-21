from django.contrib import admin
from .models import Usuario, Parceiro, Modalidade, Fichas

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Parceiro)
admin.site.register(Modalidade)
admin.site.register(Fichas)