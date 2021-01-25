from django.shortcuts import render

# Create your views here.
from web.models import Carro


def index(request):
    lista_carros = Carro.objects.all().filter(visible=True)
    ctx = {'lista_carros': lista_carros}
    return render(request, 'index.html', context=ctx)
