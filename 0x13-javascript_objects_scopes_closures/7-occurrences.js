#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.reduce((l, s) => (s === searchElement ? l + 1 : l), 0);
};
