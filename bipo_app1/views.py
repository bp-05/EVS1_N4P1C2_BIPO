from django.shortcuts import render
from django.http import HttpResponse

def vista1(request):
    html="""
    <h1 style='color:blue'>Esta es la vista 1 de la aplicacion bipo_app1</h1><br>
    <a href="/v2a1">Ir a la vista 2 de la aplicacion bipo_app1</a><br>
    <a href="/v1a2">Ir a la vista 1 de la aplicacion bipo_app2</a><br>
    <a href="/v2a2">Ir a la vista 2 de la aplicacion bipo_app2</a><br>
    """
    return HttpResponse(html)


def vista2(request):
    html="""
    <h1 style='color:red'>Esta es la vista 2 de la aplicacion bipo_app1</h1><br>
    <a href="http://127.0.0.1:8000/">Ir a la vista 1 de la aplicacion bipo_app1</a><br>
    <a href="/v1a2">Ir a la vista 1 de la aplicacion bipo_app2</a><br>
    <a href="/v2a2">Ir a la vista 2 de la aplicacion bipo_app2</a><br>
    """
    return HttpResponse(html) 

# Create your views here.
