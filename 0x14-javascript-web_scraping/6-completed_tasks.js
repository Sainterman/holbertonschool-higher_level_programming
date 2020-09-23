#!/usr/bin/node

const req = require('request');

req.get(process.argv[2], function (err, resp, body) {
  if (resp.statusCode === 200) {
    const todos = JSON.parse(body);
    const completed = {};
    todos.forEach(todo => {
      completed[todo.userId] = 0;
    });
    todos.forEach(todo => {
      if (todo.completed === true) {
        completed[todo.userId]++;
      }
    });
    console.log(completed);
  } else { console.log(err); }
});
