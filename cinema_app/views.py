from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from itertools import islice

import base64 # teste upload imagem

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db import connections
from django.db.models.signals import post_save

from cinema_app.forms import ExibicaoForm, FilmeForm, SalaForm, ArtigoForm, CinemaForm
from .models import Filme, Sala, Exibicao, Artigo, Cinema, Avaliacao

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def pagina_principal(request):
    FilmeList = Filme.objects.raw("SELECT * FROM filme")
    ArtigoList = Artigo.objects.raw("SELECT * FROM artigo")
    context = {'filme_list':FilmeList[:4] , 'artigo_list':ArtigoList[:3]}

    return render(request, 'cinema_app/pagina_principal.html', context)


# CRUD de Filmes

@login_required
def filme_form(request, filme_id=-1, filme_nome=""):
    if request.method == 'GET':
        if filme_id == -1: # está mostrando a tela de cadastro
            form = FilmeForm()
        else: # está preenchendo um filme
            filme = Filme.objects.get(pk=filme_id)
            form = FilmeForm(instance=filme)

        return render(request, 'cinema_app/filme_form.html', {'form': form})
    else:


        nome = request.POST.get('nome')
        ano_lancamento = int(request.POST.get('ano_lancamento'))
        duracao_min =  int(request.POST.get('duracao_min'))
        nome_diretor = request.POST.get('nome_diretor')
        elenco = request.POST.get('elenco')
        genero = request.POST.get('genero')
        sinopse = request.POST.get('sinopse')
        


        if filme_id == -1:
            form = FilmeForm(request.POST, request.FILES)
        else:
            filme = Filme.objects.get(pk=filme_id)
            form = FilmeForm(request.POST, request.FILES, instance=filme)

        if form.is_valid():
            cursor = connections['default'].cursor()


            
            if(len(request.FILES) != 0):
                imagem = request.FILES['poster_img'].read()
                poster_img_blob = base64.b64encode(imagem)
                poster = request.FILES['poster_img']
                query = """ INSERT INTO filme(nome, ano_lancamento, duracao_min, nome_diretor, poster_img, poster_img_blob, elenco, genero, sinopse) 
                            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s);
                """
                cursor.execute(query, [nome, ano_lancamento, duracao_min, nome_diretor, poster, poster_img_blob, elenco, genero, sinopse])
            else:
                query = """ INSERT INTO filme(nome, ano_lancamento, nome_diretor, elenco, genero, sinopse) 
                            VALUES(%s, %s, %s, %s, %s, %s, %s);
                """
                cursor.execute(query, [nome, ano_lancamento, duracao_min, nome_diretor, elenco, genero, sinopse])
            

            
            

        return HttpResponseRedirect('/filmes')


@login_required
def filme_list(request, filme_nome=""):
   
    if request.GET.get('filme_nome') != None:
        filmes = Filme.objects.raw("SELECT * FROM filme WHERE nome LIKE \'%%{}%%\'".format(request.GET.get('filme_nome')))
    else:
        filmes = Filme.objects.raw("SELECT * FROM filme")

    context = {'filme_list': filmes}

    return render(request, 'cinema_app/filme_list.html', context)

@login_required
def filme_delete(request, filme_id=-1):
    if filme_id != -1:
        cursor = connections['default'].cursor()
        cursor.execute("DELETE FROM exibicao WHERE exibicao.codigo_filme_id = %s;",[filme_id])
        cursor.execute("DELETE FROM filme WHERE filme.id = %s;",[filme_id])

    return HttpResponseRedirect('/filmes')

def filme_view(request, filme_id=-1):
    context = {}
    if(filme_id != -1):
        cursor = connections['default'].cursor()

        context['filme']= Filme.objects.get(pk=filme_id)
        cursor.execute("SELECT * FROM filme, exibicao WHERE exibicao.codigo_filme_id = %s;",[filme_id])
        context['exibicoes'] = dictfetchall(cursor)

        cursor.execute("SELECT * FROM cinema, exibicao WHERE exibicao.codigo_filme_id = %s AND exibicao.codigo_cinema_id = cinema.id;",[filme_id])
        context['cinemas'] = dictfetchall(cursor)

        cursor.execute("SELECT * FROM sala, exibicao WHERE exibicao.codigo_filme_id = %s AND exibicao.codigo_sala_id = sala.id;",[filme_id])
        context['salas'] = dictfetchall(cursor)

    return render(request, 'cinema_app/filme.html', context)

def exibicao_view(request, exibicao_id=-1):
    context = {}
    if(exibicao_id != -1):
        cursor = connections['default'].cursor()
        
        context['exibicao'] = Exibicao.objects.get(pk=exibicao_id)
        cursor.execute("SELECT * FROM filme, exibicao WHERE filme.id = exibicao.codigo_filme_id AND exibicao.id = %s;",[exibicao_id])
        context['filme'] = dictfetchall(cursor)

        cursor.execute("SELECT * FROM sala ,exibicao WHERE exibicao.id = %s and exibicao.codigo_sala_id = sala.id;",[exibicao_id])
        context['sala'] = dictfetchall(cursor)

        cursor.execute("SELECT * FROM  cinema, exibicao WHERE exibicao.id = %s and cinema.id = exibicao.codigo_cinema_id;",[exibicao_id])
        context['cinema'] = dictfetchall(cursor)

        id = context['exibicao']
        print(id)
        #cursor.execute("SELECT * FROM assento WHERE assento.codigo_sala_id = %s;", [id] )
        #context['assentos'] = dictfetchall(cursor)
        
        
    return render(request, 'cinema_app/exibicao.html', context)

def artigo_all(request):
    context = {'artigos': Exibicao.objects.raw("SELECT * FROM artigo")}
    
        
    return render(request, 'cinema_app/artigos.html', context)

def artigo_view(request, artigo_id=-1):
    context = {}
    
    if(artigo_id != -1):
        context['artigo'] = Artigo.objects.get(pk=artigo_id)
        
    return render(request, 'cinema_app/artigo.html', context)


# CRUD de Salas

@login_required
def sala_list(request):
    context = {'sala_list': Sala.objects.raw("SELECT * FROM sala")}

    return render(request, 'cinema_app/sala_list.html', context)

@login_required
def sala_form(request, sala_id=-1):
    if request.method == 'GET':
        if sala_id == -1: # está mostrando a tela de cadastro
            form = SalaForm()
        else: # está preenchendo um sala
            sala = Sala.objects.get(pk=sala_id)
            form = SalaForm(instance=sala)
        return render(request, 'cinema_app/sala_form.html', {'form': form})
    else:
        numero_assentos = int(request.POST.get('numero_assentos'))
        codigo_cinema = int(request.POST.get('codigo_cinema'))
        sessao_3d = request.POST.get('sessao_3d') == 'on'
        sessao_normal = request.POST.get('sessao_normal') == 'on'
        sessao_platinum = request.POST.get('sessao_platinum') == 'on'

        if sala_id == -1:
            form = SalaForm(request.POST)
        else:
            sala = Sala.objects.get(pk=sala_id)
            form = SalaForm(request.POST, instance=sala)

        if form.is_valid():
            cursor = connections['default'].cursor()
            query = """ INSERT INTO sala(numero_assentos, codigo_cinema_id, sessao_3d, sessao_normal, sessao_platinum) 
                            VALUES(%s, %s, %s, %s, %s);
            """
            cursor.execute(query, [numero_assentos, codigo_cinema, sessao_3d, sessao_normal, sessao_platinum])
            cursor.execute("SELECT LAST_INSERT_ID();")
            inst = (cursor.fetchone())
            sala = Sala.objects.get(pk=inst[0])
            post_save.send(sender=Sala, instance=sala, created=True)

        return HttpResponseRedirect('/salas')

@login_required
def sala_delete(request, sala_id=-1):
    if sala_id != -1:
        cursor = connections['default'].cursor()
        cursor.execute("DELETE FROM exibicao WHERE exibicao.codigo_sala_id = %s;",[sala_id])
        cursor.execute("DELETE FROM assento WHERE assento.codigo_sala_id = %s;",[sala_id])
        cursor.execute("DELETE FROM sala WHERE sala.id = %s;",[sala_id])
        # exibicao = Sala.objects.get(pk=sala_id)
        # exibicao.delete()

    return HttpResponseRedirect('/salas')


# CRUD de Exibições

@login_required
def exibicao_list(request):
    context = {'exibicao_list': Exibicao.objects.raw("SELECT * FROM exibicao")}

    return render(request, 'cinema_app/exibicao_list.html', context)

@login_required
def exibicao_form(request, exibicao_id=-1):
    if request.method == 'GET':
        if exibicao_id == -1: # está mostrando a tela de cadastro
            form = ExibicaoForm()
        else: # está preenchendo um sala
            exibicao = Exibicao.objects.get(pk=exibicao_id)
            form = ExibicaoForm(instance=exibicao)
        return render(request, 'cinema_app/exibicao_form.html', {'form': form})
    else:
        codigo_filme = int(request.POST.get('codigo_filme'))
        codigo_sala = int(request.POST.get('codigo_sala'))
        codigo_cinema = int(request.POST.get('codigo_cinema'))
        audio = request.POST.get('audio')
        legenda = request.POST.get('legenda')
        data = request.POST.get('data')
        hora = request.POST.get('hora')
        

        if exibicao_id == -1:
            form = ExibicaoForm(request.POST)
        else:
            exibicao = Exibicao.objects.get(pk=exibicao_id)
            form = ExibicaoForm(request.POST, instance=exibicao)

        if form.is_valid():
            cursor = connections['default'].cursor()
            query = """ INSERT INTO exibicao(codigo_filme_id, codigo_sala_id, codigo_cinema_id, audio, legenda, data, hora) 
                            VALUES(%s, %s, %s, %s, %s, %s, %s);
            """
            cursor.execute(query, [codigo_filme, codigo_sala, codigo_cinema, audio, legenda, data, hora])

        return HttpResponseRedirect('/exibicoes')

@login_required
def exibicao_delete(request, exibicao_id=-1):
    if exibicao_id != -1:
        cursor = connections['default'].cursor()
        cursor.execute("DELETE FROM exibicao WHERE exibicao.id = %s;",[exibicao_id])

    return HttpResponseRedirect('/exibicoes')

#CRUD de Artigo

@login_required
def artigo_list(request):
    context = {'artigo_list': Artigo.objects.raw("SELECT * FROM artigo")}

    return render(request, 'cinema_app/artigo_list.html', context)

@login_required
def artigo_form(request, artigo_id=-1):
    if request.method == 'GET':
        if artigo_id == -1: # está mostrando a tela de cadastro
            form = ArtigoForm()
        else: # está preenchendo um sala
            artigo = Artigo.objects.get(pk=artigo_id)
            form = ArtigoForm(instance=artigo)
        return render(request, 'cinema_app/artigo_form.html', {'form': form})
    else:

        if artigo_id == -1:
            form = ArtigoForm(request.POST, request.FILES)
        else:
            artigo = Artigo.objects.get(pk=artigo_id)
            form = ArtigoForm(request.POST, request.FILES, instance=artigo)

        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/artigos')


        
        
        



@login_required
def artigo_delete(request, artigo_id=-1):
    if artigo_id != -1:
        cursor = connections['default'].cursor()
        cursor.execute("DELETE FROM artigo WHERE artigo.id = %s;",[artigo_id])

    return HttpResponseRedirect('/artigos')

#CRUD do Cinema

@login_required
def cinema_list(request):
    query = """SELECT * FROM cinema;"""

    context = {'cinema_list': Cinema.objects.raw(query)}

    return render(request, 'cinema_app/cinema_list.html', context)

@login_required
def cinema_form(request, cinema_id=-1):
    if request.method == 'GET':
        if cinema_id == -1: # está mostrando a tela de cadastro
            form = CinemaForm()
        else: # está preenchendo um sala
            cinema = Cinema.objects.get(pk=cinema_id)
            form = CinemaForm(instance=cinema)
        return render(request, 'cinema_app/cinema_form.html', {'form': form})
    else:
        cnpj = request.POST.get('cnpj')
        nome = request.POST.get('nome')
        endereco = request.POST.get('endereco')
        cep = int(request.POST.get('cep'))
        numero = int(request.POST.get('numero'))
        cidade = request.POST.get('cidade')
        estado = request.POST.get('estado')
        codigo_admin = int(request.POST.get('codigo_admin'))

        if cinema_id == -1:
            form = CinemaForm(request.POST, request.FILES)
        else:
            cinema = Cinema.objects.get(pk=cinema_id)
            form = CinemaForm(request.POST, request.FILES, instance=cinema)

        if form.is_valid():
            cursor = connections['default'].cursor()
            query = """ INSERT INTO cinema(cnpj, nome, endereco, cep, numero, cidade, estado, codigo_admin_id) 
                            VALUES(%s, %s, %s, %s, %s, %s, %s, %s);
            """
            cursor.execute(query, [cnpj, nome, endereco, cep, numero, cidade, estado , codigo_admin])
        return HttpResponseRedirect('/cinemas')

            

@login_required
def cinema_delete(request, cinema_id=-1):
    if cinema_id != -1:
        cursor = connections['default'].cursor()
        cursor.execute("DELETE FROM cinema WHERE cinema.id = %s;",[cinema_id])

    return HttpResponseRedirect('/cinemas')

def avaliar_filme(request):
    if request.method == 'POST':
        el_id = request.POST.get('el_id')
        val = request.POST.get('val')

        aval = Avaliacao.objects.get(id=el_id)
        aval.nota = val
        aval.save()

        return JsonResponse({'success':'true', 'nota': val}, safe=False)
    return JsonResponse({'success':'false'})
