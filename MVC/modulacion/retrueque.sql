


CREATE DATABASE retrueque;

use retrueque;

CREATE TABLE usuario(

idUsuario int PRIMARY KEY NOT NULL AUTOINCREMENTAL,
email varchar (50) NOT NULL,
nombre varchar (100) NOT NULL,
apellido varchar(50) NOT NULL,
telefono varchar(15) NOT NULL,
password varchar(20) NOT NULL,
edad  date,
fotoPerfil  varbinary(2mb),
nivelUsario int NOT NULL)

CREATE TABLE producto(

idProducto  int PRIMARY KEY NOT NULL AUTOINCREMENTAL,
descripcion varchar(150) NOT NULL,
fotoProducto varbinary(2mb),
categoria varchar(20) NOT NULL,
interesDeIntercambio varchar(50))

CREATE TABLE trade(

idTransaccion int PRIMARY KEY NOT NULL AUTOINCREMENTAL,
tradeidUsuario int,
tradeidProducto int,
registro datetime, 
CONSTRAINT fk_idUsuario FOREIGN KEY (tradeidUsuario) 
REFERENCES usuario (idUsuario),
CONSTRAINT fk_idProducto FOREIGN KEY (tradeidProducto) 
REFERENCES producto (idProducto))