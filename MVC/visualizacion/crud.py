from sys import path

path.append('C:\\Users\\pablo\\Documents\\Ispc\\ClusterTwo\\Cluster2\\MVC')
path.append('c:\\users\\pablo\\appdata\\local\\programs\\python\\python310\\lib\\site-packages')
from controlador.dataBase import *
from controlador.usuario import *

#tablaUsuiario()
#tablaProductos()
#tablaTrade()

usuarioNuevo=cargaDeUsuario(idUsuario=1,
        email = input("Correo Electronico: "),
        nombre = input("Nombre: "),
        apellido = input("Apellido: "),
        telefono = input("telefono: "),
        password = input("ingresa clave: "),
        nivelUsuario = 0)


cambioDeContraseña(
        password=input("ingresar nueva contraseña: "),
        idUsuario= 1
        )

cambioDeEmail(
        email=input('ingrese el nuevo e-mail: '),
        idUsuario= 1
        )
