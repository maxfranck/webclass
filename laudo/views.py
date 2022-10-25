from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Documento

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def amostras(request):
    lista_amostra = Documento.objects.all()
    return render(request, 'admin/amostras.html', {'amostras': lista_amostra})

def detail(request, documento_id):
    try:
        documento = Documento.objects.get(pk=documento_id)
        documento.codigo = documento.codigo.replace('/nutrace', '/static')
    except Documento.DoesNotExist:
        raise Http404("Laudo não existe!")
    return render(request, 'laudo/detail.html', {'documento': documento})

def redirect_admin(request):
    response = redirect('laudo/documento')
    return response

def redirect_laudo(request):
    response = redirect('/admin/laudo/documento')
    return response