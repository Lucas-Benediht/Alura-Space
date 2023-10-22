from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia



# Função de requisição
def index(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True)
    #Filtrar os itens para buscar
    
    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar) #Verifica se o objeto que estamos buscando é parecido com oque vamos pesquisar
            
            
    return render(request, "galeria/buscar.html",{"cards":fotografias})


