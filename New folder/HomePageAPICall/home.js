fetch("https://www.boredapi.com/api/activity/?type=recreational")
    .then(res => res.json())
    .then(data => {
        document.getElementById('challenge').innerHTML = `${data.activity}`
    })

