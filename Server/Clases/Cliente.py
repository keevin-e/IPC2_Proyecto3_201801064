import string

class Cliente():
    NIT = string
    nombre_cliente = string
    user = string
    password = string
    direccion = string
    email = string
    lista_Instancias = list


    def __init__(self,NIT,nombre_cliente,user,password,direccion,email,lista_Instancias):
        self.NIT= NIT
        self.nombre_cliente = nombre_cliente
        self.user =user
        self.password = password
        self.direccion = direccion
        self.email = email
        self.lista_Instancias = lista_Instancias
