from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'),


    path('filmes/', views.filme_list, name='filme_list'),
    path('filme/<int:filme_id>/', views.filme_form, name='filme_update'), # get and post request for updating
    path('filme/', views.filme_form, name='filme_insert'), # get and post request for inserting
    path('filme/delete/<int:filme_id>/', views.filme_delete, name='filme_delete'),

    path('salas/', views.sala_list, name='sala_list'),
    path('sala/<int:sala_id>/', views.sala_form, name='sala_update'),
    path('sala/', views.sala_form, name='sala_insert'),
    path('sala/delete/<int:sala_id>/', views.sala_delete, name='sala_delete'),

    path('exibicoes/', views.exibicao_list, name='exibicao_list'),
    path('exibicao/<int:exibicao_id>/', views.exibicao_form, name='exibicao_update'),
    path('exibicao/', views.exibicao_form, name='exibicao_insert'),
    path('exibicao/delete/<int:exibicao_id>/', views.exibicao_delete, name='exibicao_delete'),

]
