function BuscaCep(){
    let cep = document.getElementById('cep').value
    if(cep !== "" ){
        let url = "https://brasilapi.com.br/api/cep/v1/" + cep
        
        let request = new XMLHttpRequest();
        request.open("GET", url)
        request.send()

        // trata a resposta 
        request.onload = function(){
            if(request.status === 200){
                let end = JSON.parse(request.response)
                document.getElementById('estado').value = end.state
                document.getElementById('rua').value = end.street
                document.getElementById('bairro').value = end.neighborhood
                document.getElementById('cidade').value = end.city
            } else if (request.status === 404) {
                alert("Cep inválido!")
            } else {
                alert("Erro na requisição")
            }
        }
    }
}

window.onload = function(){
    let txtcep =  document.getElementById('cep')
    txtcep.addEventListener("blur", BuscaCep)
}

$(document).ready(function() {
    //Mascara De Telefones
    $("#tel").mask('(00) 00000-0000')
    $('#tel').attr('placeholder', '(00) 00000-0000')
    $("#tel2").mask('(00) 00000-0000')
    $('#tel2').attr('placeholder', '(00) 00000-0000')

    // Mascara De cpf
    $("#cpf-mask").mask('000.000.000-00')
    $('#cpf-mask').attr('placeholder', '000.000.000-00')

    //Mascara De Cep
    $("#cep").mask('00000-000')
    $('#cep').attr('placeholder', '00000-000')
})