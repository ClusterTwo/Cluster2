from sys import path
path.append('c:\\users\\pablo\\appdata\\local\\programs\\python\\python310\\lib\\site-packages')
import mysql.connector 

#cargar usuario
nuevoUsuario = User(
        email = input("Correo Electronico: "),
        nombre = input("Nombre: "),
        apellido = input("Apellido: "),
        telefono = input("telefono: "),
        fotoPerfil= "imagen",
        password = input("ingresa clave: "),
        nivelUsuario = input("ingrese el valor de usuario: ")
        localidad = input('ingresa tu ciudad: ')
        )
      
#cambio de correo electronico
def cambioDeEmail(email,idUsuario):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='retrueque',
            user='root',
            password='')

        updateDato = f" UPDATE email SET email='{email}' WHERE idUsuario={idUsuario};"
        
        cursor = connection.cursor()
        cursor.execute(updateDato)
        connection.commit()
        print(cursor.rowcount, "email actualizado") 
    except mysql.connector.Error as error:
        print("Failed to delete record into MySQL table {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Cierre de conexion")

#cambio de contraseña
def cambioDeContraseña(password,idUsuario):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='retrueque',
            user='root',
            password='')

        updateDato = f" UPDATE email SET password ='{password}' WHERE idUsuario={idUsuario};"
        
        cursor = connection.cursor()
        cursor.execute(updateDato)
        connection.commit()
        print(cursor.rowcount, "contraseña actualizado") 
    except mysql.connector.Error as error:
        print("Failed to delete record into MySQL table {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Cierre de conexion")

#baja de de la cuenta

#validar identidad

