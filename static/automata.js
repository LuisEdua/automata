function automata(inputString) {
    // Verifica si la longitud de la cadena es 8 caracteres
    if (inputString.length !== 8) {
        alert("La cadena debe tener exactamente 8 caracteres.");
        return;
    }

    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var rawData = JSON.stringify({
        "st": inputString
    });

    var requestOptions = {
        method: 'POST',
        headers: myHeaders,
        body: rawData,
        redirect: 'follow'
    };

    fetch("/logica", requestOptions)
        .then(response => response.json())
        .then(result => {
            var resultElement = document.getElementById('result');
            var explanationElement = document.getElementById('explanation');
            var routeElement = document.getElementById('route');

            if (result.status === true) {
                resultElement.innerHTML = `<label id="green">${inputString}</label>`;
                explanationElement.textContent = "Esta cadena es válida.";

                routeElement.textContent = ">" + result.route.join("->");
            } else {
                var greenPart = inputString.slice(0, result.position);
                var redPart = inputString.slice(result.position);
                resultElement.innerHTML = `<label id="green">${greenPart}</label><label id="red">${redPart}</label>`;
                explanationElement.textContent = `Esta cadena es inválida desde la posición ${result.position + 1}.`;

                routeElement.textContent = ">" + result.route.join("->");
            }
        })
        .catch(error => console.log('error', error));
}

