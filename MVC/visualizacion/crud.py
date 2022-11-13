from sys import path
path.append('C:\\Users\\pablo\\Documents\\Ispc\\ClusterTwo\\Cluster2\\MVC')
path.append('c:\\users\\pablo\\appdata\\local\\programs\\python\\python310\\lib\\site-packages')

from modulacion.clases import *
from controlador.baseDatos import *


#instanciadorBaseDatos()
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
        email = 'pablo@asdasd',#input("Correo Electronico: "),
        nombre = 'pablo',#input("Nombre: "),
        apellido = 'montoya',#input("Apellido: "),
        telefono = '239482347',#input("telefono: "),
        fotoPerfil= "imagen",
        password = 'asdo78asd7',#input("ingresa clave: "),
        nivelUsuario = 1, #int(input("ingrese el valor de usuario: "))
        localidad = "Cordoba"
        )

nuevoUsuario.cargaDeProducto(
        descripcion = input("ingrese una leve descripcion del producto: "),
        categoria = input("cual es su categoria: "),
        interesDeIntercambio = input("porque desea intercambiar: "),
        fotoProducto= "imagen",
        idUsuario= nuevoUsuario.idUsuario,
        estadoProducto= "disponible"
        )

##tablaEstadosproductos(nuevoUsuario.idUsuario, nuevoUsuario.nuevoProducto.idProducto)