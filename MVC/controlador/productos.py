from sys import path
path.append('C:\\Users\\pablo\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages')
import mysql.connector 

#instanciar un nuevo producto
def cargaDeProducto(
    descripcion,
    categoria,
    interesDeIntercambio
):
    connection=mysql.connector.connect(
    host='localhost',
    database='retrueque',
    user='root',
    password='')

    cursor = connection.cursor()
    insertDato = """INSERT INTO productos ( descripcion, categoria, interesDeIntercambio) 
                                VALUES ( %s, %s, %s, %s, %s, %s) """
    record = (  descripcion, categoria, interesDeIntercambio)
    cursor.execute(insertDato, record)
    connection.commit()
    cursor.close()
    connection.close()

#eliminar posteo


#concretar truque

#pausar posteo por denuncia/usuario

#


