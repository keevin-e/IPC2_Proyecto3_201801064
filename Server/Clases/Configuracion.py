import string

class Configuracion():
    id_config = string
    nombre_config = string
    descripcion_config = string
    lista_recursos = list

    def __init__(self,id_config,nombre_config,descripcion_config,lista_recursos):
        self.id_config=id_config
        self.nombre_config = nombre_config
        self.descripcion_config =descripcion_config
        self.lista_recursos = lista_recursos
    
