#!/usr/bin/node

const req = require('request');

req.get('https://swapi-api.hbtn.io/api/films', function (err, resp, body) {
  if (resp.statusCode === 200) {
    let count = 0;
    const films = JSON.parse(body).results;
    films.forEach(film => {
      film.characters.forEach(character => {
        if (parseInt(character.split('/')[character.split('/').length - 2]) === 18) { count++; }
      });
    });
    console.log(count);
  } else { console.log(err); }
});
