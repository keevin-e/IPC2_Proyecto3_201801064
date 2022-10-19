from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.

def homepage(request):
    resp= requests.get('https://jsonplaceholder.typicode.com/users')
    
    #convert reponse data into json
    users = resp.json()
    print(users)
    return render(request, "home.html",{'users': users})

def carga_files(request):
    
    return render(request, "carga.html")