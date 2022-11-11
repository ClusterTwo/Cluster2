from sys import path
path.append('C:\\Users\\pablo\\Documents\\Ispc\\ClusterTwo\\Cluster2\\MVC\\modulacion')
path.append('C:\\Users\\pablo\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages')
import mysql.connector 


connection = mysql.connector.connect (
    host='localhost',
    database='retrueque',
    user='root',
    password='')
cursor = connection.cursor()

#crear tablas

try:
    
    def tablaUsuiario():
        connection=mysql.connector.connect(
        host='localhost',
        database='retrueque',
        user='root',
        password='')
        crearTablaUsuario = """ CREATE TABLE usuario(

                idUsuario int PRIMARY KEY AUTO_INCREMENT,
                email varchar(50) NOT NULL,
                nombre varchar(100) NOT NULL,
                apellido varchar(50) NOT NULL,
                telefono varchar(15) NOT NULL,
                password varchar(20) NOT NULL,
                edad date,
                nivelUsario int)
            """
        cursor = connection.cursor()
        result = cursor.execute(crearTablaUsuario)
        print("tabla Usuario creada con exito,,!! ")
        cursor.close()
        connection.close()

except mysql.connector.Error as error:
    print("Fallo al crear la tabla in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Fin de conneccion con MySQL")

try:        
    def tablaProductos():
        connection=mysql.connector.connect(
        host='localhost',
        database='retrueque',
        user='root',
        password='')
        crearTablaProducto = """ CREATE TABLE productos(

                idProducto  int PRIMARY KEY NOT NULL AUTO_INCREMENT,
                descripcion varchar(150) NOT NULL,
                categoria varchar(20) NOT NULL,
                interesDeIntercambio varchar(50))
            """
        cursor = connection.cursor()
        result = cursor.execute(crearTablaProducto)
        print("tabla Producto creada con exito,,!! ")
        cursor.close()
        connection.close()

except mysql.connector.Error as error:
    print("Fallo al crear la tabla in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Fin de conneccion con MySQL")


try:
    def tablaTrade():
        connection=mysql.connector.connect(
        host='localhost',
        database='retrueque',
        user='root',
        password='')
        crearTablaTrade = """ CREATE TABLE trade(

                idTransaccion int PRIMARY KEY NOT NULL AUTO_INCREMENT,
                tradeidUsuario int,
                tradeidProducto int,
                registro datetime, 
                CONSTRAINT fk_idUsuario FOREIGN KEY (tradeidUsuario) 
                REFERENCES usuario (idUsuario),
                CONSTRAINT fk_idProducto FOREIGN KEY (tradeidProducto) 
                REFERENCES productos (idProducto))
            """
        cursor = connection.cursor()
        result = cursor.execute(crearTablaTrade)
        print("tabla Trade creada con exito,,!! ")    
        cursor.close()
        connection.close()

except mysql.connector.Error as error:
    print("Fallo al crear la tabla in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Fin de conneccion con MySQL")        




#consultas de usuarios

#update de usuario

#delete users

#carga de productos

#update de productos

#consultas de productos

#delete productos
