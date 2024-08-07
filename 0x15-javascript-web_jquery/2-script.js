// Script that updates the text color of the header element
// Ensure the script runs only after the document is fully loaded
$(document).ready(function () {
  // Add a click event listener to the DIC with ID red_header
  $('#red_header').on('click', function () {
    // change the element to red
    $('header').css('color', '#FF0000');
  });
});
