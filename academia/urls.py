from django.contrib import admin 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('form_parceiro', views.form_parceiro, name="form_parceiro"),
    path('form_cliente', views.form_cliente, name="form_cliente"),
    path('menu_admin', views.menu_admin, name="menu_admin"),
    path('menu_cliente', views.menu_cliente, name="menu_cliente"),
    path('listagem_cliente', views.listagem_cliente, name="listagem_cliente"),
    path('agendamento_cliente', views.agendamento_cliente, name="agendamento_cliente"),
    path('edit/<int:id>', views.editlist, name="edit-cadastro"),
    path('delete/<int:id>', views.deletelist, name="delete-cadastro"),
    path('financeiro_cliente', views.financeiro_cliente, name="financeiro_cliente"),
    path('modalidades', views.modalidades, name='modalidades'),
    path('cadastro_modalidade', views.cadastroModalidade, name='cadastro_modalidade')
]