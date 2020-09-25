$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  const movies = data.results;
  movies.forEach(movie => {
    $(`<li>${movie.title}</li>`).appendTo('UL#list_movies');
  });
}, 'json');
