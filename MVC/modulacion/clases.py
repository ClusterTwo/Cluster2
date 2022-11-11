from email.mime import image
from errno import EADDRNOTAVAIL


class User():
    idUsuario = ""
    email = ""
    password = ""
    nombre = ""
    apellido = ""
    telefono = 0
    edad = 0
    #fotoPerfil = image
    nivelUsuario = ""


    def __init__(self, email, password, 
        nombre, apellido, telefono, edad):

        self.email = email
        self.password = password
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.edad = edad
        
    
    def cargaProducto(): #instancia un producto
        newProducto = producto()
        return "se cargo el nuevo producto"
        

    def retiroProducto(self):
        pass

    def confirmarTrade(self):
        pass

class producto():
    idProducto =1
    descripcion = ""
    fotoProducto = "una imagen" #image
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


nuevoUsuario= User
nuevoUsuario.cargaProducto(            
    descripcion=input('Ingrese una breve descripcion: '),
    categoria=input('Ingrese a que categoria pertenece: '),
    interesDeIntercambio=input('Porque producto te interesa intercambiar: ')
    )    
