import string

class Consumo():
    nit_cliente = string
    id_Instancia = string
    tiempo_consumido = float
    fecha_hora = string

    def __init__(self,nit_cliente,id_Instancia,tiempo_consumido,fecha_hora):
        self.nit_cliente= nit_cliente
        self.id_Instancia = id_Instancia
        self.tiempo_consumido =tiempo_consumido
        self.fecha_hora = fecha_hora
    
    def get_nit_cliente (self):
        return self.nit_cliente 
    
    def set_nit_cliente (self, nit_cliente):
        self.nit_cliente = nit_cliente
    
    def get_id_Instancia (self):
        return self.id_Instancia 
    
    def set_id_Instancia (self, id_Instancia):
        self.id_Instancia = id_Instancia
    
    def get_tiempo_consumido (self):
        return self.tiempo_consumido 
    
    def set_tiempo_consumido (self, tiempo_consumido):
        self.tiempo_consumido = tiempo_consumido
    
    def get_fecha_hora (self):
        return self.fecha_hora 
    
    def set_fecha_hora (self, fecha_hora):
        self.fecha_hora = fecha_hora