#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w === undefined || h === undefined) {
      return;
    }

    if (w <= 0 || h <= 0) {
      return this;
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      const text = 'X';
      console.log(text.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
