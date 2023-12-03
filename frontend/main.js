
function makeRequest() {
    const param1Value = document.getElementById('input11').value;
    const param2Value = document.getElementById('input12').value;

    const param3Value = document.getElementById('input21').value;
    const param4Value = document.getElementById('input22').value;
  
    const apiUrl = 'localhost:5000/';
    const params = { 
      origen: [param1Value, param2Value],
      destino: [param3Value, param4Value]
    };
  
    const queryString = new URLSearchParams(params).toString();
    const urlWithParams = `${apiUrl}?${queryString}`;
  
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
  