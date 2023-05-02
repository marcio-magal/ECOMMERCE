from django.shortcuts import render


def loja_1(request):
    return render(request, 'lojas/loja-1.html')

def loja_2(request):
    return render(request, 'lojas/loja-2.html')

def loja_3(request):
    return render(request, 'lojas/loja-3.html')
