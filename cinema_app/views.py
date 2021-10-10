from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

from cinema_app.forms import ExibicaoForm, FilmeForm, SalaForm
from .models import Filme, Sala, Exibicao


def pagina_principal(request):
    return render(request, 'cinema_app/pagina_principal.html')


# CRUD de Filmes

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


# CRUD de Salas

def sala_list(request):
    context = {'sala_list': Sala.objects.all()}

    return render(request, 'cinema_app/sala_list.html', context)

def sala_form(request, sala_id=-1):
    if request.method == 'GET':
        if sala_id == -1: # está mostrando a tela de cadastro
            form = SalaForm()
        else: # está preenchendo um sala
            sala = Sala.objects.get(pk=sala_id)
            form = SalaForm(instance=sala)
        return render(request, 'cinema_app/sala_form.html', {'form': form})    
    else:
        if sala_id == -1:
            form = SalaForm(request.POST)
        else:
            sala = Sala.objects.get(pk=sala_id)
            form = SalaForm(request.POST, instance=sala)

        if form.is_valid():
            form.save()

        return HttpResponseRedirect('/salas')

def sala_delete(request, sala_id=-1):
    if sala_id != -1:
        sala = Sala.objects.get(pk=sala_id)
        sala.delete()
    
    return HttpResponseRedirect('/salas')


# CRUD de Exibições

def exibicao_list(request):
    context = {'exibicao_list': Exibicao.objects.all()}

    return render(request, 'cinema_app/exibicao_list.html', context)

def exibicao_form(request, exibicao_id=-1):
    if request.method == 'GET':
        if exibicao_id == -1: # está mostrando a tela de cadastro
            form = ExibicaoForm()
        else: # está preenchendo um sala
            exibicao = Exibicao.objects.get(pk=exibicao_id)
            form = ExibicaoForm(instance=exibicao)
        return render(request, 'cinema_app/exibicao_form.html', {'form': form})    
    else:
        if exibicao_id == -1:
            form = ExibicaoForm(request.POST)
        else:
            exibicao = Exibicao.objects.get(pk=exibicao_id)
            form = ExibicaoForm(request.POST, instance=exibicao)

        if form.is_valid():
            form.save()

        return HttpResponseRedirect('/exibicoes')

def exibicao_delete(request, exibicao_id=-1):
    if exibicao_id != -1:
        exibicao = Exibicao.objects.get(pk=exibicao_id)
        exibicao.delete()
    
    return HttpResponseRedirect('/exibicoes')


