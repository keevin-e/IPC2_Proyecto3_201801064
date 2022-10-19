import string

class Recurso():
    id_recurso = string
    nombre_recurso = string
    abreviatura_recurso = string
    metrica = string
    tipo = string
    costo = float

    def __init__(self,id_recurso,nombre_recurso,abreviatura_recurso,metrica,tipo,costo):
        self.id_recurso=id_recurso
        self.nombre_recurso = nombre_recurso
        self.abreviatura_recurso =abreviatura_recurso
        self.metrica =metrica
        self.tipo = tipo
        self.costo = costo
    
    ''' def get_id_recurso (self):
        return self.id_recurso 
    
    def set_id_recurso (self, id_recurso):
        self.id_recurso = id_recurso
    
    def get_nombre_recurso (self):
        return self.nombre_recurso 
    
    def set_nombre_recurso (self, nombre_recurso):
        self.nombre_recurso = nombre_recurso
    
    def get_metrica (self):
        return self.metrica 
    
    def set_metrica (self, metrica):
        self.metrica = metrica
    
    def get_tipo (self):
        return self.tipo 
    
    def set_tipo (self, tipo):
        self.tipo = tipo
    
    def get_costo (self):
        return self.costo 
    
    def set_costo (self, costo):
        self.costo = costo '''