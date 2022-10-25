from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from xml.dom import minidom
from .forms import config_form, consume_form
from django.contrib import messages
import json
import requests

# Create your views here.
def consulta_page(request):
    return render(request, "consulta.html")

def carga_files(request):
    message =''
    if request.method == 'POST':
        if request.POST.get('config_file') != None:
            form = config_form(request.POST)
            if form.is_valid():
                data = request.POST.get('config_file')
                response= send_configFile(data)
                messg= response['categorias']+' '+response['clientes']+' '+response['recursos']
                print(response)
                message = messg
        else:
            form = consume_form(request.POST)
            if form.is_valid():
                data = request.POST.get('consumo_file')
                response= send_consumoFile(data)['consumos']
                message = response
    else:
        form = config_form()
       
    return render(request, "carga.html", {'form': form, 'message':message})

def send_configFile(data):
    request = requests.post('http://127.0.0.1:5000/post-config', json={'data': data})
    return json.loads(request.text)

def send_consumoFile(data):
    request = requests.post('http://127.0.0.1:5000/post-consumos', json={'data': data})
    return json.loads(request.text)

def consulta_Categorias(request):
    resp= requests.get('http://127.0.0.1:5000/get-categorias')
    
     #convert reponse data into json
    data = resp.json()
    return render(request, "view-catg.html",{'categorias': data})

def consulta_clientes(request):
   resp= requests.get('http://127.0.0.1:5000/get-clientes')
   data = resp.json()
   return render(request, "view-clientes.html",{'clientes': data})

def consulta_recursos(request):
    resp= requests.get('http://127.0.0.1:5000/get-recursos')
    data = resp.json()
    return render(request, "view-recursos.html",{'recursos': data})

def creacion_page(request):
    return render(request, "creacion_dash.html")

def crear_recurso(request):
    return render(request, "crear_recurso.html")