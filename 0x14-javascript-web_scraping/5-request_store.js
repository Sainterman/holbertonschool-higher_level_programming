#!/usr/bin/node

const req = require('request');
const fs = require('fs');

req.get(process.argv[2], function (err, resp, body) {
  if (resp.statusCode === 200) {
    fs.writeFile(process.argv[3], body, function (err) {
      if (err) console.log(err);
    });
  } else { console.log(err); }
});
