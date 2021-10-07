from django.urls import path 
from . import views

urlpatterns = [ 
    path('filmes/', views.filme_list, name='filme_list'),
    path('filme/<int:filme_id>/', views.filme_form, name='filme_update'), # get and post request for updating
    path('filme/', views.filme_form, name='filme_insert'), # get and post request for inserting
    path('filme/delete/<int:filme_id>/', views.filme_delete, name='filme_delete')
]