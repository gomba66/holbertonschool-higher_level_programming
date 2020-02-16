$(document).ready(function () {
  $.getJSON('https://swapi.co/api/films/?format=json', function (result) {
    let i = 0;
    const movies = result.results;
    while (i < movies.length) {
      $('UL#list_movies').append('<li>' + movies[i].title + '</li>');
      i++;
    }
  });
});
