CREATE DATABASE retrueque;
USE retrueque ;


CREATE TABLE usuario (
  idUsuario INT PRIMARY KEY AUTO_INCREMENT,
  email VARCHAR(255) NOT NULL,
  password VARCHAR(32) NOT NULL,
  edad DATETIME NULL,
  nombre VARCHAR(50) NOT NULL,
  apellido VARCHAR(50) NOT NULL,
  telefono varchar(13) NULL,
  fotoPerfil LONGBLOB NULL,
  nivelUsuario VARCHAR (20) NOT NULL,
  localidad VARCHAR(45) NOT NULL,
  CONSTRAINT fk_nivelUsuario 
    FOREIGN KEY (nivelUsuario) 
    REFERENCES capacidadDelUsuario (nivelDeUsuario),
  CONSTRAINT fk_localidad 
    FOREIGN KEY (localidad) 
    REFERENCES ciudad (nombreCiudad));

CREATE TABLE capacidadDelUsuario (
  nivelDeUsuario VARCHAR(20) NOT NULL,
  PRIMARY KEY (nivelDeUsuario));

CREATE TABLE ciudad (
  nombreCiudad VARCHAR(45) NOT NULL DEFAULT 'Cordoba',
  codigoPostal INT NULL,
  PRIMARY KEY (nombreCiudad));


CREATE TABLE productos (
  idProducto INT AUTO_INCREMENT,
  descripcion VARCHAR(150) NOT NULL,
  categoria VARCHAR(25) NOT NULL,
  interesDeIntercambio VARCHAR(50) NOT NULL,
  fotoProducto LONGBLOB NULL,
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
    ON UPDATE CASCADE);

CREATE TABLE estadosproductos (
  disponibilidad VARCHAR(55) NOT NULL,
  PRIMARY KEY (disponibilidad));

CREATE TABLE categorias (
  categoria VARCHAR(20) NOT NULL,
  PRIMARY KEY (categoria));



CREATE TABLE trade (
  idTransaccion INT NOT NULL,
  tradeidProducto INT NOT NULL,
  registro DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (idTransaccion),
  UNIQUE INDEX idTransaccion_UNIQUE (idTransaccion ASC) VISIBLE,
  INDEX fk_idProducto_idx (tradeidProducto ASC) VISIBLE,
  CONSTRAINT fk_idProducto
    FOREIGN KEY (tradeidProducto)
    REFERENCES productos (idProducto)
    ON DELETE NO ACTION
    ON UPDATE CASCADE,
  CONSTRAINT fk_usuario
    FOREIGN KEY (tradeidUsuario)
    REFERENCES usuario (idUsuario)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
