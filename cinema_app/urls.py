from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'),

    path('filmes/', views.filme_list, name='filme_list'),
    path('filmes/<str:filme_nome>/', views.filme_list, name='filme_search'),
    path('filme/<int:filme_id>/', views.filme_form, name='filme_update'), 
    path('filme/', views.filme_form, name='filme_insert'), 
    path('filme/delete/<int:filme_id>/', views.filme_delete, name='filme_delete'),

    path('salas/', views.sala_list, name='sala_list'),
    path('sala/<int:sala_id>/', views.sala_form, name='sala_update'),
    path('sala/', views.sala_form, name='sala_insert'),
    path('sala/delete/<int:sala_id>/', views.sala_delete, name='sala_delete'),

    path('exibicoes/', views.exibicao_list, name='exibicao_list'),
    path('exibicao/<int:exibicao_id>/', views.exibicao_form, name='exibicao_update'),
    path('exibicao/', views.exibicao_form, name='exibicao_insert'),
    path('exibicao/delete/<int:exibicao_id>/', views.exibicao_delete, name='exibicao_delete'),

    path('artigos/', views.artigo_list, name='artigo_list'),
    path('artigo/<int:artigo_id>/', views.artigo_form, name='artigo_update'),
    path('artigo/', views.artigo_form, name='artigo_insert'),
    path('artigo/delete/<int:artigo_id>/', views.artigo_delete, name='artigo_delete'),
    path('artigos-todos/', views.artigo_all, name='artigo_all'),
    path('artigos/visualizar/<int:artigo_id>/', views.artigo_view, name='artigo_view'),

    path('cinemas/', views.cinema_list, name='cinema_list'),
    path('cinema/<int:cinema_id>/', views.cinema_form, name='cinema_update'),
    path('cinema/', views.cinema_form, name='cinema_insert'),
    path('cinema/delete/<int:cinema_id>/', views.cinema_delete, name='cinema_delete'),

    path('filme/cinemas/<int:filme_id>/', views.filme_view, name='filme_view'),
    path('avaliar/', views.avaliar_filme, name='avaliar_filme'),
    path('filme/exibicao/<int:exibicao_id>/', views.exibicao_view, name='exibicao_view'),
]
