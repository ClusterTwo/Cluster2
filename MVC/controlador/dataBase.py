from readline import insert_text
import sqlite3 as sql
from tkinter import _Cursor

#generar base de datos
def creadorDeBase():
    conn = sql.connect("retrueque.db")
    conn.commit()
    conn.close()

#crear tablas
def creadorDeTablas():
    conn= sql.connect("retrueque.db")
    cursor = conn.cursor()
    cursor.execute(
        """ CREATE TABLE usuario(

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
        """ CREATE TABLE producto(

            idProducto  int PRIMARY KEY NOT NULL AUTOINCREMENTAL,
            descripcion varchar(150) NOT NULL,
            fotoProducto varbinary(2mb),
            categoria varchar(20) NOT NULL,
            interesDeIntercambio varchar(50))
        """
        """ CREATE TABLE trade(

            idTransaccion int PRIMARY KEY NOT NULL AUTOINCREMENTAL,
            tradeidUsuario int,
            tradeidProducto int,
            registro datetime, 
            CONSTRAINT fk_idUsuario FOREIGN KEY (tradeidUsuario) 
            REFERENCES usuario (idUsuario),
            CONSTRAINT fk_idProducto FOREIGN KEY (tradeidProducto) 
            REFERENCES producto (idProducto))
        """
    )

#cargar usuario
def cargaDeUsuario():
    conn= sql.connect("retrueque.db")
    cursor = conn.cursor()
    instanciaUsuario = f"INSERT INTO usuario VALUES ('{email}','{nombre}','{apellido}','{telefono}','{password}', {nivelUsuario} )"
    cursor.execute(instanciaUsuario)
    conn.commit()
    conn.close

cargaDeUsuario()

#consultas de usuarios

#update de usuario

#delete users

#carga de productos

#update de productos

#consultas de productos

#delete productos
