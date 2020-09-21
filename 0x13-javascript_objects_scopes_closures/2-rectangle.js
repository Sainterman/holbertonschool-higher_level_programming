#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w === undefined || h === undefined) {
      return;
    }
    if (w <= 0 || h <= 0) {

    } else {
      this.height = h;
      this.width = w;
    }
  }
}

module.exports = Rectangle;
