from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuario(request):
    # Salvar os dados da tela para para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    
    # exibir todos os usuarios ja cadastrados em uma nova janela
    usuarios = {
        'usuarios' : Usuario.objects.all()
    }
    # retornar os dados para a pagina de listagem de usuarios
    return render(request, 'usuarios/usuarios.html', usuarios)