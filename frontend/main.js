// Get the button element by its ID
var infoButton = document.getElementById('submitButton');

// Add an event listener to the button for the 'click' event
infoButton.addEventListener('click', function() {
  // Save information when the button is clicked
  var buttonInfo = "Button clicked at: " + new Date().toLocaleTimeString();

  // You can do something with the buttonInfo here (e.g., display it, store it, etc.)
  console.log(buttonInfo); // For demonstration, printing the info to console
});
