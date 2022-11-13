function loginValidation() {
    var userEmail, userPassword, emailValidation;

    userEmail = document.getElementById("userEmail").value;
    userPassword = document.getElementById("userPassword").value;

    emailValidation = /\w+@\w+\.+[a-z]/;
    
    if (userEmail.length>100) {
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