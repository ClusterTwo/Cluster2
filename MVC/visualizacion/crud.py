from MVC.controlador.dataBase import cargaDeUsuario

cargaDeUsuario(
    email = input("Correo Electronico: "),
    nombre = input("Nombre: "),
    apellido = input("Apellido: "),
    telefono = input("telefono: "),
    nivelUsuario = 0
)