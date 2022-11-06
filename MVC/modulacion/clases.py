from email.mime import image
from errno import EADDRNOTAVAIL


class User:
    idUsuario = ""
    email = ""
    password = ""
    nombre = ""
    apellido = ""
    telefono = 0
    edad = 0
    fotoPerfil = image
    nivelUsuario = ""


    def __init__(self, email, password, 
        nombre, apellido, telefono, edad):

        self.email = email
        self.password = password
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.edad = edad
        
    
    def cargaProducto(self,descripcion,fotoProducto,categoria,interesDeIntercambio): #instancia un producto
        self.newProducto = producto (
            descripcion=input('Ingrese una breve descripcion: '),
            fotoProducto=input(),
            categoria=input('Ingrese a que categoria pertenece: '),
            interesDeIntercambio=input('Porque producto te interesa intercambiar: ')
            )
        

    def retiroProducto(self):
        pass

    def confirmarTrade(self):
        pass

class producto:
    idProducto = 0
    descripcion =""
    fotoProducto = image
    categoria = ""
    interesDeIntercambio = ""

    def __init__(self, 
        descripcion,
        fotoproducto,
        categoria,
        interesDeIntercambio):
        self.descripcion = descripcion
        self.fotoProducto = fotoproducto
        self.categoria = categoria
        self.interesDeIntercambio = interesDeIntercambio
    
    def correccionDatos(self):
        pass
