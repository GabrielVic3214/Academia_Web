function BuscaCep(){
    let cep = document.getElementById('txtcep').value
    if(cep !== "" ){
        let url = "https://brasilapi.com.br/api/cep/v1/" + cep
        
        let request = new XMLHttpRequest();
        request.open("GET", url)
        request.send()

        // trata a resposta 
        request.onload = function(){
            if(request.status === 200){
                let end = JSON.parse(request.response)
                document.getElementById('txtestado').value = end.state
                document.getElementById('txtrua').value = end.street
                document.getElementById('txtbairro').value = end.neighborhood
            } else if (request.status === 404) {
                alert("Cep inválido!")
            } else {
                alert("Erro na requisição")
            }
        }
    }
}

window.onload = function(){
    let txtcep =  document.getElementById('txtcep')
    txtcep.addEventListener("blur", BuscaCep)
}