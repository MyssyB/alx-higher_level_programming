// Script that add <li> element to a list whe a user clicks on at
// DIV#add_item
$(document).ready(function () {
  // Add event listener
  $('#add_item').on('click', function () {
    // Create a new <li> element
    const NewItem = $('<li>Item</li>');
    // Append the new <li> element
    $('UL.my_list').append(NewItem);
  });
});
