from sys import path
path.append('C:\\Users\\pablo\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages')
import mysql.connector

connection = mysql.connector.connect (
    host='localhost',
    database='retrueque',
    user='root',
    password='')
cursor = connection.cursor()

#crear tablas

#Tabla Usuario
try:
    def tablaUsuario():
        connection=mysql.connector.connect(
            host='localhost',
            database='retrueque',
            user='root',
            password='')

        crearTablaUsuario = """ CREATE TABLE usuario (
            idUsuario INT PRIMARY KEY AUTO_INCREMENT,
            email VARCHAR(255) NOT NULL,
            password VARCHAR(32) NOT NULL,
            edad DATETIME NULL,
            nombre VARCHAR(50) NOT NULL,
            apellido VARCHAR(50) NOT NULL,
            telefono VARCHAR(13) NULL,
            fotoPerfil VARCHAR(25) NULL,
            nivelUsuario VARCHAR(20) NOT NULL,
            localidad VARCHAR(45) NOT NULL,
            CONSTRAINT fk_nivelUsuario FOREIGN KEY (nivelUsuario) REFERENCES capacidadDelUsuario (nivelDeUsuario),
            CONSTRAINT fk_localidad FOREIGN KEY (localidad) REFERENCES ciudad (nombreCiudad)
            );"""
        cursor = connection.cursor()
        result = cursor.execute(crearTablaUsuario)
        print("tabla Usuario creada con exito! ")
        cursor.close()
        connection.close()

except mysql.connector.Error as error:
    print("Fallo al crear la tabla in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Fin de conneccion con MySQL")

#tabla ciudad
try:
    
    def tablaCiudad():
        connection=mysql.connector.connect(
        host='localhost',
        database='retrueque',
        user='root',
        password='')
        crearTablaUsuario = """  CREATE TABLE ciudad (
            nombreCiudad VARCHAR(45) NOT NULL DEFAULT 'Cordoba Capital',
            codigoPostal INT NULL,
            PRIMARY KEY (nombreCiudad));  """
        cursor = connection.cursor()
        result = cursor.execute(crearTablaUsuario)
        print("tabla ciudad creada con exito! ")
        cursor.close()
        connection.close()

except mysql.connector.Error as error:
    print("Fallo al crear la tabla in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Fin de conneccion con MySQL")

#tabla permisos del usuario
try:
    
    def tablaCapacidadDelUsuario():
        connection=mysql.connector.connect(
        host='localhost',
        database='retrueque',
        user='root',
        password='')
        crearTablaUsuario = """  CREATE TABLE capacidadDelUsuario (
            nivelDeUsuario VARCHAR(20) NOT NULL,
            PRIMARY KEY (nivelDeUsuario));  """
        cursor = connection.cursor()
        result = cursor.execute(crearTablaUsuario)
        print("tabla capacidadDelUsuario creada con exito! ")
        cursor.close()
        connection.close()

except mysql.connector.Error as error:
    print("Fallo al crear la tabla in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Fin de conneccion con MySQL")

#tabla Productos
try:        
    def tablaProductos():
        connection=mysql.connector.connect(
        host='localhost',
        database='retrueque',
        user='root',
        password='')
        crearTablaProducto = """ CREATE TABLE productos (
            idProducto INT AUTO_INCREMENT,
            descripcion VARCHAR(150) NOT NULL,
            categoria VARCHAR(25) NOT NULL,
            interesDeIntercambio VARCHAR(50) NOT NULL,
            fotoProducto VARCHAR(25) NULL,
            usuarioProducto INT NOT NULL,
            estadoProducto VARCHAR(45) NULL,
            PRIMARY KEY (idProducto),
            UNIQUE INDEX idProducto_UNIQUE (idProducto ) ,
            INDEX fk_usuario_idx (usuarioProducto ) ,
            INDEX fk_categorias_idx (categoria ) ,
            CONSTRAINT fk_usuario
              FOREIGN KEY (usuarioProducto)
              REFERENCES usuario (idUsuario)
              ON DELETE CASCADE
              ON UPDATE CASCADE,
            CONSTRAINT fk_categorias
              FOREIGN KEY (categoria)
              REFERENCES categorias (categoria)
              ON DELETE NO ACTION
              ON UPDATE CASCADE,
            CONSTRAINT fk_estadoproducto
              FOREIGN KEY (estadoProducto)
              REFERENCES estadosproductos (disponibilidad)
              ON DELETE NO ACTION
              ON UPDATE CASCADE);  """
        cursor = connection.cursor()
        result = cursor.execute(crearTablaProducto)
        print("tabla Productos creada con exito,,!! ")
        cursor.close()
        connection.close()

except mysql.connector.Error as error:
    print("Fallo al crear la tabla in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Fin de conneccion con MySQL")

#tabla disponibilidad del producto
try:
    
    def tablaEstadosproductos():
        connection=mysql.connector.connect(
        host='localhost',
        database='retrueque',
        user='root',
        password='')
        crearTablaUsuario = """  CREATE TABLE estadosproductos (
            disponibilidad VARCHAR(55) NOT NULL,
            PRIMARY KEY (disponibilidad));  """
        cursor = connection.cursor()
        result = cursor.execute(crearTablaUsuario)
        print("tabla estadosproductos creada con exito! ")
        cursor.close()
        connection.close()

except mysql.connector.Error as error:
    print("Fallo al crear la tabla in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Fin de conneccion con MySQL")

#tabla categoriasproducto
try:
    
    def tablaCategorias():
        connection=mysql.connector.connect(
        host='localhost',
        database='retrueque',
        user='root',
        password='')
        crearTablaUsuario = """  CREATE TABLE categorias (
            categoria VARCHAR(20) NOT NULL,
            PRIMARY KEY (categoria));  """
        cursor = connection.cursor()
        result = cursor.execute(crearTablaUsuario)
        print("tabla categorias creada con exito! ")
        cursor.close()
        connection.close()

except mysql.connector.Error as error:
    print("Fallo al crear la tabla in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Fin de conneccion con MySQL")

#tabla Trade
try:
    def tablaTrade():
        connection=mysql.connector.connect(
        host='localhost',
        database='retrueque',
        user='root',
        password='')
        crearTablaTrade = """ CREATE TABLE trade (
            idTransaccion INT PRIMARY KEY AUTO_INCREMENT,
            tradeidProducto INT NOT NULL,
            tradeidUsuario INT NOT NULL,
            registro DATE NOT NULL,
            CONSTRAINT fk_idProducto
              FOREIGN KEY (tradeidProducto)
              REFERENCES productos (idProducto)
              ON DELETE NO ACTION
              ON UPDATE CASCADE,
            CONSTRAINT fk_tradeidUsuario 
              FOREIGN KEY (tradeidUsuario) 
              REFERENCES usuario (idUsuario) 
              ON DELETE NO ACTION 
              ON UPDATE CASCADE);"""
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



def insertarNivelesUsuarios(nivel1,nivel2,nivel3):
    connection=mysql.connector.connect(
    host='localhost',
    database='retrueque',
    user='root',
    password='')
    cursor = connection.cursor()
    insertDato = """INSERT INTO capacidadDelUsuario (nivelDeUsuario) 
                                VALUES (%s) """
    records_to_insert = [(nivel1),(nivel2),(nivel3)]
    cursor.executemany(insertDato, records_to_insert)
    connection.commit()
    print('se insertaron los datos en capacidadDelUsuario')
    cursor.close()
    connection.close()

def insertarCiudades(ciudad1,ciudad2,ciudad3):
    connection=mysql.connector.connect(
    host='localhost',
    database='retrueque',
    user='root',
    password='')
    cursor = connection.cursor()
    insertDato = """INSERT INTO ciudad (nombreCiudad) 
                                VALUES (%s) """
    records_to_insert = [(ciudad1),(ciudad2),(ciudad3)]
    cursor.executemany(insertDato, records_to_insert)
    connection.commit()
    print('se insertaron los datos en ciudad')
    cursor.close()
    connection.close()

def insertarEstados(estado1,estado2,estado3,estado4):
    connection=mysql.connector.connect(
    host='localhost',
    database='retrueque',
    user='root',
    password='')
    cursor = connection.cursor()
    insertDato = """INSERT INTO estadosproductos (disponibilidad) 
                                VALUES (%s)"""
    records_to_insert = [(estado1),(estado2),(estado3),(estado4)]
    cursor.executemany(insertDato, records_to_insert)
    connection.commit()
    print('se insertaron los datos en estadosProductos')
    cursor.close()
    connection.close()

def insertarCategoria(categoria1,categoria2,categoria3,categoria4):
    connection=mysql.connector.connect(
    host='localhost',
    database='retrueque',
    user='root',
    password='')
    cursor = connection.cursor()
    insertDato = """INSERT INTO categorias (categoria) 
                                VALUES (%s) """
    records_to_insert = [(categoria1),
                        (categoria2),
                        (categoria3),
                        (categoria4)]
    cursor.executemany(insertDato, records_to_insert)
    connection.commit()
    print('se insertaron los datos en categorias')
    cursor.close()
    connection.close()    


#consultas de usuarios

#update de usuario


#delete users

#carga de productos

#update de productos

#consultas de productos

#delete productos


#consultas de usuarios

#update de usuario

#delete users

#carga de productos

#update de productos

#consultas de productos

#delete productos
