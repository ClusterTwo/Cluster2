function regValidation() {
    var userName, userLastName, userPhone, userEmail, userPassword, emailValidation;

    userName = document.getElementById("userName").value;
    userLastName = document.getElementById("userLastName").value;
    userPhone = document.getElementById("userPhone").value;
    userEmail = document.getElementById("userEmail").value;
    userPassword = document.getElementById("userPassword").value;

    emailValidation = /\w+@\w+\.+[a-z]/;

    if (userName === "" || userLastName === "" || userPhone === "" || userEmail === "" || userPassword === "") {
        alert("Todos los campos son obligatorios.");
        return false;
    }
    else if (userName.length>30) {
        alert("El nombre es muy largo.")
        return false;
    }
    else if (userLastName.length>60) {
        alert("El apellido es muy largo.")
        return false;
    }
    else if (userPhone.length>18) {
        alert("El teléfono es muy largo.")
        return false;
    }
    else if (isNaN(userPhone)) {
        alert("El teléfono ingresado no es un número")
        return false;
    }
    else if (userEmail.length>100) {
        alert("El correo es muy largo.")
        return false;
    }
    else if (!emailValidation.test(userEmail)){
        alert("El correo ingresado no es válido")
        return false;
    }
    else if (userPassword.length<8) {
        alert("La contraseña debe tener un mínimo de 8 caracteres.")
        return false;
    }
    else if (userPassword.length>16) {
        alert("La contraseña debe tener un máximo de 16 caracteres.")
        return false;
    }
}
