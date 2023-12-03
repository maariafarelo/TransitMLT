
function makeRequest() {
    const param1Value = document.getElementById('input11').value;

    const param3Value = document.getElementById('input21').value;
  
    const apiUrl = 'http://localhost:5000/';
    const params = { 
      origen: "[" + param1Value + "]",
      destino: "[" + param3Value + "]"
    };
  
    const queryString = new URLSearchParams(params).toString();
    const urlWithParams = `${apiUrl}?origen=[${param1Value}]&destino=[${param3Value}]`;
  
    fetch(urlWithParams)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        // Handle the data received from the API
        console.log(data);
      })
      .catch(error => {
        // Handle any errors that occurred during the fetch
        console.error('There was a problem with the fetch operation:', error);
      });
  }
  