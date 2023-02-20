from django.shortcuts import render

def index(request):
    return render(request, 'lojas/index.html')

def loja_1(request):
    return render(request, 'lojas/Loja_1.html')

def loja_2(request):
    return render(request, 'lojas/Loja_2.html')

def loja_3(request):
    return render(request, 'lojas/Loja_3.html')
