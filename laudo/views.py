from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render

from .models import Documento

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, documento_id):
    try:
        documento = Documento.objects.get(pk=documento_id)
        documento.codigo = documento.codigo.replace('/nutrace', '/static/polls')
    except Documento.DoesNotExist:
        raise Http404("Laudo não existe!")
    return render(request, 'laudo/detail.html', {'documento': documento})
