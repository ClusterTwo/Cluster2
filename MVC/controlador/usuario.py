from sys import path
path.append('c:\\users\\pablo\\appdata\\local\\programs\\python\\python310\\lib\\site-packages')
import mysql.connector 

#cambio de correo electronico
def cambioDeEmail(email,idUsuario):
    try:
        connection = mysql.connector.connect(host='localhost',
        database='retrueque.sql',
        user='admin',
        password='admin')

        mySql_insert_query = f" UPDATE email SET email='{email}' WHERE idUsuario={idUsuario};"
        
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
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
        connection = mysql.connector.connect(host='localhost',
        database='retrueque.sql',
        user='admin',
        password='admin')

        mySql_insert_query = f" UPDATE password SET password ='{password}' WHERE idUsuario={idUsuario};"
        
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query)
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

