from sys import path

path.append('C:\\Users\\pablo\\Documents\\Ispc\\ClusterTwo\\Cluster2\\MVC')
path.append('c:\\users\\pablo\\appdata\\local\\programs\\python\\python310\\lib\\site-packages')
from controlador.dataBase import *
#from controlador.usuario import *
from modulacion.clases import *

tablaUsuario()
tablaProductos()
tablaTrade()
#
#usuarioNuevo=cargaDeUsuario(
#        email = input("Correo Electronico: "),
#        nombre = input("Nombre: "),
#        apellido = input("Apellido: "),
#        telefono = input("telefono: "),
#        password = input("ingresa clave: "),
#        nivelUsuario = 1)
#
#
#cambioDeContraseña(
#        password=input("ingresar nueva contraseña: "),
#        idUsuario= 1
#        )
#
#cambioDeEmail(
#        email=input('ingrese el nuevo e-mail: '),
#        idUsuario= 1
#        )
#
nuevoUsuario = User(
        email = input("Correo Electronico: "),
        nombre = input("Nombre: "),
        apellido = input("Apellido: "),
        telefono = input("telefono: "),
        password = input("ingresa clave: "),
        nivelUsuario = int(input("ingrese el valor de usuario: "))
)

nuevoUsuario.cargaDeProducto(
        descripcion=input('ingrese una leve descripcion del producto:'),
        categoria = input('cual es su categoria: '),
        interesDeIntercambio=input('porque desea intercambiar: '))