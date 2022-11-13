from sys import path
path.append('C:\\Users\\pablo\\Documents\\Ispc\\ClusterTwo\\Cluster2\\MVC')
path.append('c:\\users\\pablo\\appdata\\local\\programs\\python\\python310\\lib\\site-packages')
from modulacion.dataBase import *
from modulacion.clases import *
from controlador.baseDatos import *


instanciadorBaseDatos()
insertarCategoria(['calzados'],['camperas'],['plantas'],['herramientas'])
insertarCiudades(["Cordoba"],["CABA"],["Rosario"])
insertarEstados(['disponible'],['en pausa'],['trocado'],['eliminado'])
insertarNivelesUsuarios(['eventual'],['registrado'],['administrador'])

nuevoUsuario = User(
        email = 'pmontoasdya@gmial.com',#input("Correo Electronico: "),
        nombre = 'pablo',#input("Nombre: "),
        apellido = 'montoya',#input("Apellido: "),
        telefono = '239482347',#input("telefono: "),
        fotoPerfil= "imagen",
        password = 'asdo78asd7',#input("ingresa clave: "),
        nivelUsuario = 'registrado', #input("ingrese el valor de usuario: "))
        localidad = "Cordoba"
        )

nuevoUsuario.cargaDeProducto(
        descripcion="zapatillas",#input("ingrese una leve descripcion del producto: "),
        categoria = "calzados",#input("cual es su categoria: "),
        interesDeIntercambio = "pantalones",#input("porque desea intercambiar: "),
        fotoProducto= "imagen",
        idUsuario = nuevoUsuario.consultaId(nuevoUsuario.email),
        estadoProducto= "disponible"
        )

nuevoUsuario.cambioDeContraseña(
        password=input("ingresar nueva contraseña: "),
        idUsuario = nuevoUsuario.consultaId(nuevoUsuario.email)
        )

nuevoUsuario.cambioDeEmail(
        email=input('ingrese el nuevo e-mail: '),
        idUsuario = nuevoUsuario.consultaId(nuevoUsuario.email)
        )

##tablaEstadosproductos(nuevoUsuario.idUsuario, nuevoUsuario.nuevoProducto.idProducto)