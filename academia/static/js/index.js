document.getElementById("login-form").addEventListener('submit', function(event){
    event.preventDefault()

    const form = document.getElementById("login-form")
    const formData = new FormData(form)

    fetch("/login/", {
        method: 'POST',
        body: formData
    })
    .then(Response => {
        if (Response.ok){
            window.location.href = "/dashboard/"
        } else {
            console.error("Falha no login")
        }
    })
    .catch(error => {
        console.error("Erro de rede: ", error)
    })
})