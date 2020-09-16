#!/usr/bin/node

const args = process.argv;
const times = parseInt(args[2]);
if (isNaN(times)) {
  console.log('Missing number of ocurrences');
}
for (let index = 0; index < times; index++) {
  console.log('C is fun');
}
