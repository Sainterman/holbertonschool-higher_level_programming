#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
request.get(`https://swapi-api.hbtn.io/api/films/${id}`, function (response, err, body) {
  if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else { console.log(err); }
});
