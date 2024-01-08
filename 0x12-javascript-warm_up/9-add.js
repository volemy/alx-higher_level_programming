#!/usr/bin/node
const myVar1 = parseInt(process.argv[2]);
const myVar2 = parseInt(process.argv[3]);

function add (x, y) {
  if (isNaN(x) || isNaN(y)) {
    return NaN;
  }
  return x + y;
}

console.log(add(myVar1, myVar2));
