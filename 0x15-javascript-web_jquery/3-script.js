// Script that adds the class red to the header element when the user clicks
$(document).ready(function () {
  // Add a click even listener to the DIV with the ID red_header
  $('#red_header').on('click', function () {
    // Add the 'red text'
    $('header').addClass('red-text');
  });
});
