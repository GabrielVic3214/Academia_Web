from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from .models import Modalidade, Usuario, Parceiro
from .forms import UserForm, Form_Parceiro, FormModalidade
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
# Create your views here.



def Index(request):

    return render(request, 'main/index.html')

def form_parceiro(request):

    if request.method == 'POST':
        form = Form_Parceiro(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return HttpResponse('Ocorreu um erro!!')

    else:
        form = Form_Parceiro()
        return render(request, 'main/Form_Parceiro.html', {'form': form})
    


def form_cliente(request):
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('listagem_cliente')
        else:
            return HttpResponse('Ocorreu um erro no save')

    else:
        form = UserForm()
        return render(request, 'main/Form_Cliente.html', {'form': form})


def menu_admin(request):
    user = request.user
    return render(request, 'main/tela_inicial_admin.html', {'user': user})

def menu_cliente(request):
    return render(request, 'main/tela_inicial_cliente.html')

def listagem_cliente(request):
    users = Usuario.objects.all()
    return render(request, 'main/tela_listagem_cliente.html', {'users': users})

def agendamento_cliente(request):
    return render(request, 'main/Agendamento_cliente.html')

def financeiro_cliente(request):
    return render(request, 'main/financeiroCliente.html')

def editlist(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    form = UserForm(instance=usuario)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=usuario)

        if form.is_valid():
            usuario.save()
            return redirect('listagem_cliente')
        else:
            return HttpResponse("Occoreu um erro na edição")

    else:
        return render(request, 'main/editcadastro.html', {'form': form, 'usuario': usuario})
    
def deletelist(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    usuario.delete()

    messages.info(request, 'O usuario foi deletado com sucesso')

    return redirect('listagem_cliente')

def modalidades(request):
    modalidades = Modalidade.objects.all()
    return render(request, 'main/modalidades.html', {'modalidades': modalidades})

def cadastroModalidade(request):
    form = FormModalidade()
    modalidades = Modalidade.objects.all()
    if request.method == "POST":
        form = FormModalidade(request.POST)
        if form.is_valid():
            form.save()
            return redirect('menu_admin')
        else:
            return HttpResponse('ocorreu um erro')
    else:
        return render(request, 'main/cadastro_modalidades.html', {'form': form, 'modalidades': modalidades})
    
