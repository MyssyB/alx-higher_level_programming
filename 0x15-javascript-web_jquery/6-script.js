// Script that runs when the document is ready
$(document).ready(function () {
  // Add a click event listener to the 'DIV#update_eader'
  $('#update_header').on('click', function () {
    // Update the text of the header
    $('header').text('New Header!!!');
  });
});
