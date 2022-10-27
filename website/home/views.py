from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from xml.dom import minidom
from .forms import config_form, consume_form , crearRecurso_form ,crearConfig_form
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

def consulta_configuraciones(request):
    resp= requests.get('http://127.0.0.1:5000/get-configuraciones')
    data = resp.json()
    return render(request, "view-config.html",{'configuraciones': data})

def creacion_page(request):
    return render(request, "creacion_dash.html")

def crear_recurso(request):
    message =''
    if request.method == 'POST':
        form = crearRecurso_form(request.POST)
        if form.is_valid():
            nombre = request.POST.get('nombre_recurso')
            abreviatura = request.POST.get('abreviatura')
            tipo = request.POST.get('tipo')
            metrica = request.POST.get('metrica')
            costo = request.POST.get('costo')
            id = request.POST.get('id')
            
            dato ={
               'id':id,
               'nombre':nombre,
               'abreviatura':abreviatura,
               'metrica':metrica,
               'tipo':tipo,
               'costo':costo
            }
            response = sendCrear_recurso(dato)
            message = response['message']
            

    else:
        form = crearRecurso_form()    
    
    return render(request, "crear_recurso.html", {'form': form,'message':message})

def sendCrear_recurso(data):
    request = requests.post('http://127.0.0.1:5000/crear-recurso', json={'data': data})
    return json.loads(request.text)


def crear_config(request):
    message =''
    recursos = requests.get('http://127.0.0.1:5000/get-recursos')
    data = recursos.json()
    
    if request.method == 'POST':

        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        id = request.POST['id']
        recursos = request.POST['recursos']
        cantidad = request.POST['cantidad']
        
        dato ={
           'id':id,
           'nombre':nombre,
           'descripcion':descripcion,
           'recursos':recursos,
           'cantidad':cantidad
        }
        response = sendCrear_config(dato)
        message = response['message']
        return render(request, "crear-config.html", {'message':message})    

    else:
        recursos = requests.get('http://127.0.0.1:5000/get-recursos')
        data = recursos.json()
        return render(request, "crear-config.html", {'message':message,'recursos':data})
    

def sendCrear_config(data):
    request = requests.post('http://127.0.0.1:5000/crear-configuracion', json={'data': data})
    return json.loads(request.text)
