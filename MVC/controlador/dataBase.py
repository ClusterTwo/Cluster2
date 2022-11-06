import mysql.connector
import MVC.modulacion.reTrueque.sql

connection=mysql.connector.connect(
    host='localhost',
    database='Retrueque.sql',
    user='admin',
    password='admin')

try:
    #crear tablas
    def tablaUsuiario():
        connection=mysql.connector.connect(
        host='localhost',
        database='Retrueque.sql',
        user='admin',
        password='admin')
        mySql_Create_Table_Query = """ CREATE TABLE usuario(

                idUsuario int PRIMARY KEY NOT NULL AUTOINCREMENTAL,
                email varchar (50) NOT NULL,
                nombre varchar (100) NOT NULL,
                apellido varchar(50) NOT NULL,
                telefono varchar(15) NOT NULL,
                password varchar(20) NOT NULL,
                edad  date,
                fotoPerfil  varbinary(2mb),
                nivelUsario int NOT NULL)
            """
        cursor = connection.cursor()
        result = cursor.execute(mySql_Create_Table_Query)
        print("tabla productos creada con exito,,!! ")
        cursor.close()
        connection.close()

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
try:        
    def tablaProductos():
        connection=mysql.connector.connect(
        host='localhost',
        database='Retrueque.sql',
        user='admin',
        password='admin')
        mySql_Create_Table_Query = """ CREATE TABLE producto(

                idProducto  int PRIMARY KEY NOT NULL AUTOINCREMENTAL,
                descripcion varchar(150) NOT NULL,
                fotoProducto varbinary(2mb),
                categoria varchar(20) NOT NULL,
                interesDeIntercambio varchar(50))
            """
        cursor = connection.cursor()
        result = cursor.execute(mySql_Create_Table_Query)
        print("tabla productos creada con exito,,!! ")
        cursor.close()
        connection.close()

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

try:
    def tablaTrade():
        connection=mysql.connector.connect(
        host='localhost',
        database='Retrueque.sql',
        user='admin',
        password='admin')
        mySql_Create_Table_Query = """ CREATE TABLE trade(

                idTransaccion int PRIMARY KEY NOT NULL AUTOINCREMENTAL,
                tradeidUsuario int,
                tradeidProducto int,
                registro datetime, 
                CONSTRAINT fk_idUsuario FOREIGN KEY (tradeidUsuario) 
                REFERENCES usuario (idUsuario),
                CONSTRAINT fk_idProducto FOREIGN KEY (tradeidProducto) 
                REFERENCES producto (idProducto))
            """
        cursor = connection.cursor()
        result = cursor.execute(mySql_Create_Table_Query)
        print("tabla productos creada con exito,,!! ")    
        cursor.close()
        connection.close()

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")        


#cargar usuario
def cargaDeUsuario():
    connection=mysql.connector.connect(
    host='localhost',
    database='Retrueque.sql',
    user='admin',
    password='admin')
    cursor = connection.cursor()
    mySql_insert_query = """INSERT INTO productos (idUsuario, email, nombre, apellido, telefono, password, nivelUsuario) 
                                VALUES (%s, %s, %s, %s) """
    record = (idUsuario, email, nombre, apellido, telefono, password, nivelUsuario)
    cursor.execute(mySql_insert_query, record)
    connection.commit()
    cursor.close()
    connection.close()
    

#consultas de usuarios

#update de usuario

#delete users

#carga de productos

#update de productos

#consultas de productos

#delete productos
