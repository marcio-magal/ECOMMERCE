from django.shortcuts import render

def index(request):
    return render(request, 'produtos/index.html')

def carrinho(request):
    return render(request, 'produtos/carrinho.html')
