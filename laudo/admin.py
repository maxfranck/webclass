from django.contrib import admin

from .models import Documento

class DocumentoAdmin(admin.ModelAdmin):
    fields = ['amostra_id', 'cultura']
    list_display = ('amostra_id', 'cultura')

admin.site.register(Documento, DocumentoAdmin)