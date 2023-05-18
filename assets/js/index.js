function logar(){
    let user = document.getElementById("userLogin").value;
    let senha = document.getElementById("senhaLogin").value;
    if(user == "admin" && senha == 1){
        window.location.href = "TelaInicialAdmin.html";
    } else if(user == "user" && senha == 1){
        window.location.href = "TelaInicialUsuario.html";
    } else{
        alertOn();
        document.getElementById("userLogin").value = "";
        document.getElementById("senhaLogin").value = "";
    }
} 

function alertOff(){
    document.getElementById("alertaLogin").classList.add("displayNone")
}
function alertOn(){
    document.getElementById("alertaLogin").classList.remove("displayNone")
    setTimeout(alertOff, 3000);
}