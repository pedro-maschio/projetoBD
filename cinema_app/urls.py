from django.urls import path 
from . import views

urlpatterns = [ 
    path('filme/<int:filme_id>/', views.detail, name='detail'),
    path('filmes/', views.index, name='index'),
    path('filmes/cadastro', views.cadastroFilme, name='cadastroFilme')
]