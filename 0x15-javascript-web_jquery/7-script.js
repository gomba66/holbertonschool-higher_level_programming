$(document).ready(function () {
  $.getJSON('https://swapi.co/api/people/5/?format=json', function (result) { $('div').text(result.name); });
});
