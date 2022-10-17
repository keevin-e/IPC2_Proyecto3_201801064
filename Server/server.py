from flask import Flask, request,jsonify
from flask_restful import Api
from flask_cors import CORS, cross_origin
import json
from dotenv import load_dotenv

from Clases.Categoria import Categoria


app = Flask(__name__)
CORS(app)
api = Api(app)
load_dotenv()

Categorias = [] #lista simple


#login
''' @app.route('/home/login', methods=['POST']) '''
@app.route('/', methods=['GET'])
def getUser():
    return "Hello world"

#subir archivo Configuraciones
@app.route('/subir-listaconfig', methods=['POST'])
def subirListaConfig():
    pass


#Crear Configuracion
@app.route('/crear-configuracion', methods=['POST'])
def createConfiguracion():
    global Categorias
    id = request.json['id_categ']
    nombre = request.json['nombre_categ']
    descripcion_categ = request.json['descripcion_categ']
    carga_de_trabajo = request.json['carga_de_trabajo']
    lista_config = request.json['lista_config']
    
    nuevaConfig = Categoria(id,nombre, descripcion_categ, carga_de_trabajo,lista_config)
    Categorias.append(nuevaConfig)
    
    Dato = {
                'message': 'Configuracion agregada Exitosamente',
                'state':'Success'
            }
    respuesta = jsonify(Dato)
    return (respuesta)



if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.run(host="0.0.0.0", port="5000")

#./venv/Scripts/activate   
#export FLASK_APP=server.py
# cd server
#python -m flask run


#------- Django ---------------
#cd website
#py manage.py runserver 3000
#py manage.py --help
''' crear apps/pages/componentes/paginas '''
#py manage.py startapp login
#django-admin.py startapp Login