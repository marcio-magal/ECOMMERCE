from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def estabelecimentos(request):
    return HttpResponse('Estabelecimentos')

def loja_1(request):
    return HttpResponse('Loja 1')

def loja_2(request):
    return HttpResponse('Loja 2')
