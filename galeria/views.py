from django.shortcuts import render


# Cuidar da exibição do servidor

# Função de requisição
def index(request):
    return render(request, 'galeria/index.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')

