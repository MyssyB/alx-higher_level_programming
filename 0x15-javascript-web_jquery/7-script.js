// Ensure the script runs after the document is full loaded
$(document).ready(function() {
	// Fetch the JSON data from the URL
	$.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {...}
		// Extract the name from the url data
		var characterName = data.name;
		// Display the character name in the DIV#character
		$('#character').text(characterName);
});
