from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse
from .models import Filme

# Create your views here.

def detail(request, filme_id):  
    try:
        filme = Filme.objects.get(pk=filme_id)
    except Filme.DoesNotExist:
        raise Http404("Este filme não existe")
    return render(request, 'cinema/detalheFilme.html', {'filme': filme})    


def index(request):
    latest_movies = Filme.objects.order_by('-ano_lancamento')[:5]
    
    return render(request, 'cinema/index.html', {'filmes': latest_movies})

def cadastroFilme(request):
    pass
