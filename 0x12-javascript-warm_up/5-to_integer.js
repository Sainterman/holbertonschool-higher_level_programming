#!/usr/bin/node

const args = process.argv;
const parsd = parseInt(args[2], 10);
if (isNaN(parsd)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parsd);
}
