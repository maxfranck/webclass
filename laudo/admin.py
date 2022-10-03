from django.contrib import admin

from .models import Documento

class DocumentoAdmin(admin.ModelAdmin):
    fields = ['amostra_id', 'oferta', 'distribuidor', 'cultura']
    list_display = ('amostra_id', 'oferta', 'distribuidor', 'cultura')

admin.site.register(Documento, DocumentoAdmin)