from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

from cinema_app.forms import FilmeForm
from .models import Filme

# Create your views here.

def filme_form(request, filme_id=-1):
    
    if request.method == 'GET':
        if filme_id == -1: # está mostrando a tela de cadastro
            form = FilmeForm()
        else: # está preenchendo um filme
            filme = Filme.objects.get(pk=filme_id)
            form = FilmeForm(instance=filme)
        return render(request, 'cinema_app/filme_form.html', {'form': form})    
    else:
        if filme_id == -1:
            form = FilmeForm(request.POST)
        else:
            filme = Filme.objects.get(pk=filme_id)
            form = FilmeForm(request.POST, instance=filme)

        if form.is_valid():
            form.save()

        return HttpResponseRedirect('/filmes')
    


def filme_list(request):
    context = {'filme_list': Filme.objects.all()}
    
    return render(request, 'cinema_app/filme_list.html', context)

def filme_delete(request, filme_id=-1):
    if filme_id != -1:
        filme = Filme.objects.get(pk=filme_id)
        filme.delete()
    
    return HttpResponseRedirect('/filmes')

