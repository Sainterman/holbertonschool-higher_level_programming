#!/usr/bin/node

exports.esrever = function (list) {
  const b = list.reduceRight((a, c) => (a.push(c), a), []);
  return b;
};
