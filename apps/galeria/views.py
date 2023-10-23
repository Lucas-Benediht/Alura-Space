from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms
from django.contrib import messages



# Função de requisição
def index(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    #Filtrar os itens para buscar
    
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar) #Verifica se o objeto que estamos buscando é parecido com oque vamos pesquisar
            
            
    return render(request, "galeria/buscar.html",{"cards":fotografias})


def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, "Usuário não logado")
        return redirect('login')
    
    form = FotografiaForms
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES) # Criação da nova imagem no bd
        if form.is_valid():
            form.save()
            messages.success(request, "Nova Fotografia Cadastrada com Sucesso!")
            return redirect('index')
         
    return render(request, 'galeria/nova_imagem.html', {'form': form})

def editar_imagem(request):
    pass

def deletar_imagem(request):
    pass