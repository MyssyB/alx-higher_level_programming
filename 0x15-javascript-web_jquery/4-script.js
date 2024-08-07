// Script that toggles the class
$(document).ready(function () {
  // Add a clieck event listener to the DIV with ID
  $('#toggle_header').on('click', function () {
    // Check the current class of the eader tand toggle
    $('header').toggleClass('red green');
  });
});
