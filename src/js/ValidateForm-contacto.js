//Captura de Datos
let form = document.getElementById("formulario"),
elementos = form.elements,
boton = document.getElementById("btnSend");

//Validacion de nombre y Apellido.

validarNombre = function(e){
    if (form.names.value == 0) {
        alert("Ingrese su Nombre y Apellido")
        e.preventDefault();
    }  
}

//Validacion de E-mail
validarEmail = function(email){
    let expReg = /^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$/;
    let emailValido = expReg.test(email);
    if (emailValido == false) {
        alert('Introduzca un E-mail valido');
    }
}

// Validacion de Asunto
validarAsunto = function(e){
    if (form.asunto.value == 0) {
        alert("Ingrese un asunto, por favor");
        e.preventDefault();
    }  
}

//Validacion de Mensaje

validarMensaje = function(e){
    if (form.mensaje.value == 0) {
        alert("Ingrese un mensaje, por favor");
        e.preventDefault();
    }  
}

//Funcion validadora

let validar = function(e){
    validarNombre(e)
    validarEmail(form.email.value)
    validarAsunto(e)
    validarMensaje(e)
}


form.addEventListener("submit", validar);