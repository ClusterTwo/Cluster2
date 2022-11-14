from sys import path
path.append('C:\\Users\\pablo\\Documents\\Ispc\\ClusterTwo\\Cluster2\\MVC')
path.append('c:\\users\\pablo\\appdata\\local\\programs\\python\\python310\\lib\\site-packages')
import mysql.connector 
from controlador.productos import *
from email.mime import image
from errno import EADDRNOTAVAIL


class User():
    idUsuario = 0
    email = ""
    password = ""
    nombre = ""
    apellido = ""
    telefono = ""
    edad = 0
    fotoPerfil = "imagen"
    nivelUsuario = ""
    localidad = ""


    def __init__(self, email, password, 
        nombre, apellido,fotoPerfil, telefono, nivelUsuario, localidad):

        self.email = email
        self.password = password
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.fotoPerfil = fotoPerfil
        self.nivelUsuario = nivelUsuario
        self.localidad = localidad

        connection=mysql.connector.connect(
        host='localhost',
        database='retrueque',
        user='root',
        password='')
        cursor = connection.cursor()
        insertDato = """INSERT INTO Usuario ( email, nombre, apellido, fotoPerfil, telefono, password, nivelUsuario,localidad) 
                                    VALUES ( %s, %s, %s,%s, %s, %s, %s, %s) """
        record = ( email, nombre, apellido, fotoPerfil, telefono, password,nivelUsuario,localidad)
        cursor.execute(insertDato, record)
        connection.commit()
        print('se creo con exito la cuenta!!!')
        cursor.close()
        connection.close()

    def consultaId(self,email):
        connection = mysql.connector.connect(host='localhost',
                                                 database='retrueque',
                                                 user='root',
                                                 password='')

        consulta = f"SELECT idUsuario FROM usuario WHERE email ='{email}';" 
        cursor = connection.cursor()
        cursor.execute(consulta)
        fila=cursor.fetchall()
        numeroId = fila[0]
        idUsuario = int('.'.join(str(ele) for ele in numeroId))
        return idUsuario


    def cargaDeProducto(self,descripcion, categoria, interesDeIntercambio, fotoProducto,idUsuario,estadoProducto):
        self.nuevoProducto = producto(descripcion, categoria, interesDeIntercambio, fotoProducto,idUsuario,estadoProducto)
        return "producto cargado con exito"

    def cambioDeEmail(self,idUsuario,email):
        connection = mysql.connector.connect(
            host='localhost',
            database='retrueque',
            user='root',
            password='')
        updateDato = f" UPDATE usuario SET email ='{email}' WHERE idUsuario={idUsuario};"
        cursor = connection.cursor()
        cursor.execute(updateDato)
        connection.commit()
        print(cursor.rowcount, "email actualizado")    

    

    def cambioDeContraseña(self,idUsuario,password):
        connection = mysql.connector.connect(
            host='localhost',
            database='retrueque',
            user='root',
            password='')
        updateDato = f" UPDATE usuario SET password = '{password}' WHERE idUsuario={idUsuario};"
        cursor = connection.cursor()
        cursor.execute(updateDato)
        connection.commit()
        print(cursor.rowcount, "contraseña actualizado") 


    def retiroProducto(self):
        pass

    def confirmarTrade(self):
        pass
class producto():
    idProducto = 0
    descripcion = ""
    fotoProducto = "una imagen" #image
    categoria = ""
    interesDeIntercambio = ""
    estadoProducto = ""

    def __init__(self, 
        descripcion,
        fotoProducto,
        categoria,
        interesDeIntercambio,
        usuarioProducto,
        estadoProducto):
        self.descripcion = descripcion
        self.fotoProducto = fotoProducto
        self.categoria = categoria
        self.interesDeIntercambio = interesDeIntercambio
        self.usuarioProducto = usuarioProducto
        self.estadoProducto = estadoProducto
        connection=mysql.connector.connect(
        host='localhost',
        database='retrueque',
        user='root',
        password='')
        cursor = connection.cursor()
        insertDato = """INSERT INTO productos (descripcion, categoria, interesDeIntercambio, fotoProducto, usuarioProducto, estadoProducto) 
                                    VALUES (%s, %s, %s, %s, %s, %s) """
        record = ( descripcion, fotoProducto, categoria, interesDeIntercambio, usuarioProducto, estadoProducto)
        cursor.execute(insertDato, record)
        connection.commit()
        print('el producto fue subido con exito!!!')
        cursor.close()
        connection.close()
    
    def estadoProducto(self,idProducto,idUsuario):
        connection = mysql.connector.connect(host='localhost',
                                     database='retrueque',
                                     user='root',
                                     password='')
        consulta = f"SELECT estadoProducto FROM productos WHERE usuarioProducto = {idUsuario} AND idProducto = {idProducto}"
        cursor = connection.cursor()
        cursor.execute(consulta)
        fila=cursor.fetchall()
        print(fila)
        cursor.close()
        connection.close()
            
        def correccionDatos(self):
            pass


 
