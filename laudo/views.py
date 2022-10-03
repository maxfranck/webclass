from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, laudo_id):
    return HttpResponse("You're looking at question %s." % laudo_id)
