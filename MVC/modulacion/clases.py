from sys import path

path.append('C:\\Users\\pablo\\Documents\\Ispc\\ClusterTwo\\Cluster2\\MVC')
path.append('c:\\users\\pablo\\appdata\\local\\programs\\python\\python310\\lib\\site-packages')
import mysql.connector 
from controlador.productos import *
from email.mime import image
from errno import EADDRNOTAVAIL


class User():
    idUsuario = ""
    email = ""
    password = ""
    nombre = ""
    apellido = ""
    telefono = 0
    #edad = 0
    #fotoPerfil = image
    nivelUsuario = 0


    def __init__(self, email, password, 
        nombre, apellido, telefono, nivelUsuario):

        self.email = email
        self.password = password
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        nivelUsuario = nivelUsuario

        connection=mysql.connector.connect(
        host='localhost',
        database='retrueque',
        user='root',
        password='')
        cursor = connection.cursor()
        insertDato = """INSERT INTO Usuario ( email, nombre, apellido, telefono, password, nivelUsuario) 
                                    VALUES ( %s, %s, %s, %s, %s, %s) """
        record = ( email, nombre, apellido, telefono, password,nivelUsuario)
        cursor.execute(insertDato, record)
        connection.commit()
        cursor.close()
        connection.close()

    def cargaDeProducto(self,descripcion, categoria, interesDeIntercambio):
        self.nuevoProducto = producto(descripcion, categoria, interesDeIntercambio)
        return "producto cargado con exito"
    

    def retiroProducto(self):
        pass

    def confirmarTrade(self):
        pass

class producto():
    idProducto =1
    descripcion = ""
    #fotoProducto = "una imagen" #image
    categoria = ""
    interesDeIntercambio = ""

    def __init__(self, 
        descripcion,
        #fotoproducto,
        categoria,
        interesDeIntercambio):
        self.descripcion = descripcion
        #self.fotoProducto = fotoproducto
        self.categoria = categoria
        self.interesDeIntercambio = interesDeIntercambio
        connection=mysql.connector.connect(
        host='localhost',
        database='retrueque',
        user='root',
        password='')

        cursor = connection.cursor()
        insertDato = """INSERT INTO productos ( descripcion, categoria, interesDeIntercambio) 
                                    VALUES ( %s, %s, %s) """
        record = (  descripcion, categoria, interesDeIntercambio)
        cursor.execute(insertDato, record)
        connection.commit()
        cursor.close()
        connection.close()
    
    def correccionDatos(self):
        pass


 
