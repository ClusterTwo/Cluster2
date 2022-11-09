//Captura de datos
let form = document.getElementById("formulario"),
  elementos = form.elements,
  boton = document.getElementById("btnSend");

//Validacion de Titulo de Producto
validarTitulo = function (e) {
  if (form.names.value == 0) {
    alert("Ingrese un titulo para su producto");
    e.preventDefault();
  }
};

//Validar Descripcion
validarDescripcion = function (e) {
  if (form.descripcion.value == 0) {
    alert("Ingrese una descripcion para su producto");
    e.preventDefault();
  }
};

//Validar Interes
validarInteres = function (e) {
  if (form.interes.value == 0) {
    alert("Ingrese un interes de trueque");
    e.preventDefault();
  }
};

//Funcion validadora

let validar = function (e) {
  validarTitulo(e);
  validarDescripcion(e);
  validarInteres(e);
};

form.addEventListener("submit", validar);
