import string

class Categoria():
    id_categoria = string
    nombre_categoria = string
    descripcion_categoria = string
    carga_de_trabajo = string
    lista_configuraciones = list
    
    
    def __init__(self,id_categoria,nombre_categoria,descripcion_categoria,carga_de_trabajo,lista_configuraciones):
        self.id_categoria=id_categoria
        self.nombre_categoria = nombre_categoria
        self.descripcion_categoria =descripcion_categoria
        self.carga_de_trabajo = carga_de_trabajo
        self.lista_configuraciones = lista_configuraciones
