// ===== DARK MODE =====

function modoOscuro(){

document.body.classList.toggle("dark-mode");

/* guardar preferencia */

if(document.body.classList.contains("dark-mode")){
    localStorage.setItem("modo","oscuro");
}else{
    localStorage.setItem("modo","claro");
}

}

/* cargar modo guardado */

window.onload = function(){

if(localStorage.getItem("modo") === "oscuro"){
    document.body.classList.add("dark-mode");
}

}

// Alerta onClick

function mostrarToast(nombre,color){

let mensaje = document.getElementById("toastMensaje");

mensaje.innerText = nombre + " seleccionado!";

let toastElement = document.getElementById("pokemonToast");

toastElement.className = "toast align-items-center text-bg-" + color + " border-0";

let toast = new bootstrap.Toast(toastElement);

toast.show();

}

// Footer

function volverArriba(){

window.scrollTo({
top:0,
behavior:"smooth"
});

}

// Iframe oculto hasta que se scrollea
window.addEventListener("scroll", function(){

let iframe = document.querySelector(".fixed-iframe");

if(window.scrollY > 150){
    iframe.style.display = "none";
}else{
    iframe.style.display = "block";
}

});