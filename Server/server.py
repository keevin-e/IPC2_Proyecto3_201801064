from flask import Flask, request,jsonify
from flask_restful import Api
from flask_cors import CORS, cross_origin
import json
from dotenv import load_dotenv

from Clases.Categoria import Categoria
from Clases.Cliente import Cliente
from Clases.Configuracion import Configuracion
from Clases.Consumo import Consumo
from Clases.Instancia import Instancia
from Clases.Recurso import Recurso

app = Flask(__name__)
CORS(app)
api = Api(app)
load_dotenv()

Categorias = [] #lista
Clientes = [] #lista
Recursos = [] #lista
Consumos =[] #lista

Configuraciones_glob = []
Instancias_glob=[]



#Home
@app.route('/', methods=['GET'])
def home():
    return "Hello world"

#subir archivo Configuraciones
@app.route('/subir-config', methods=['POST'])
def subirListaConfig():
    global Recursos
    global Categorias
    global Clientes
    
    #Recursos
    recursos = request.json['listaRecursos']
    count_recursos = 0
    for rec in recursos:
        count_recursos += 1
        id_recurso = rec['id']
        nombre_recurso = rec['nombre']
        abreviatura_recurso = rec['abreviatura']
        metrica = rec['metrica']
        tipo_recurso = rec['tipo']
        costo_recurso = rec['valorXhora']

        new_Recurso = Recurso(id_recurso,nombre_recurso,abreviatura_recurso,metrica,tipo_recurso,costo_recurso)
        Recursos.append(new_Recurso)
    
    #categorias    
    categorias = request.json['listaCategorias']
    count_categ = 0
    for cat in categorias:
        Configuraciones = [] #lista
        count_categ += 1
        id_categoria = cat['id']
        nombre_categoria = cat['nombre']
        descr_categoria = cat['descripcion']
        carga_de_trabajo = cat['cargaTrabajo']
        list_config = cat['listaConfiguraciones']
        
        #configuraciones por Categoria
        count_config = 0
        for config in list_config:
            count_config += 1
            id_config = config['id']
            nombre_config = config['nombre']
            dscr_config = config['descripcion']
            recursos_config = config['recursosConfiguracion']
            
            #lista de recursos por configuracion (id's y cantidad)
            list_rec_config = []
            for rec_config in recursos_config:
                id_recurso = rec_config['id']
                cantidad_rec = rec_config['cantidadRecurso']
                recursos ={
                    "id recurso":id_recurso,
                    "cantidad":cantidad_rec
                }
                list_rec_config.append(recursos)

            new_config = Configuracion(id_config,nombre_config,dscr_config,list_rec_config)
            Configuraciones.append(new_config)
            
        new_categoria = Categoria(id_categoria,nombre_categoria,descr_categoria,carga_de_trabajo,Configuraciones)
        Categorias.append(new_categoria)    
    
    #clientes
    clientes = request.json['listaClientes']
    count_clientes = 0 
    for clt in clientes:
        count_clientes += 1
        Instancias = [] #lista
        
        NIT = clt['nit']
        nombre_cliente = clt['nombre']
        usuario = clt['usuario'] 
        clave = clt['clave'] 
        direccion = clt['direccion']
        email = clt['correoElectronico']
        instancias = clt['listaInstancias']
        
        for ins in instancias:
            id_instance = ins['id']
            id_configuracion = ins['idConfiguracion']
            nombre = ins['nombre']
            fecha_inicio = ins['fechaInicio']
            estado = ins['estado']
            fecha_final = ins['fechaFinal']
            
            new_instancia = Instancia(id_instance,id_configuracion,nombre,fecha_inicio,estado,fecha_final)
            Instancias.append(new_instancia)
            
        new_cliente = Cliente(NIT,nombre_cliente,usuario,clave,direccion,email,Instancias)
        Clientes.append(new_cliente)
    
    Dato ={
        'recursos':str(count_recursos)+' recursos añadidos',
        'categorias':str(count_categ)+' Categorias añadidas',
        'clientes':str(count_clientes)+' Clientes añadidos',
        'status':200
    }
    for i in Recursos:
        print (i.nombre_recurso)
    
    print('----------------------')
    for x in Categorias:
        print(x.nombre_categoria)    

    print('----------------------')
    for z in Clientes:
        print(z.nombre_cliente)    

    #nuevos_recursos.append(Dato)
    response =jsonify(Dato)
    return(response)
    

#subir archiv de Consumos
@app.route('/subir-consumos', methods=['POST'])
def subirConsumo():
    global Consumos
    
    consumos = request.json['listadoConsumos']
    count_consumos=0
    for cons in consumos:
        count_consumos += 1
        nitCliente = cons['nitCliente']
        idInstancia = cons['idInstancia']
        tiempo_cons = cons['tiempo']
        fecha_hora = cons['fechaHora']
        
        new_consumo = Consumo(nitCliente,idInstancia,tiempo_cons,fecha_hora)
        Consumos.append(new_consumo)

    Dato = {
                'message': 'Cosumos agregados Exitosamente',
                'consumos':str(count_consumos)+' consumos Agregados',
                'status':200
            }
    respuesta = jsonify(Dato)
    return (respuesta)


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

#. ./venv/Scripts/activate  
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