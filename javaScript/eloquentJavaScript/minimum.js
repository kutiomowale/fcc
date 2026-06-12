#!/usr/bin/env node
//The function min that takes two arguments and returns their minimum
function min(a, b) {
  return a < b ? a : b;
}
console.log("min(7, 10) =", min(7, 10));
console.log("min(10, 7) =", min(10, 7));
console.log("min(5, 5) =", min(5, 5));
console.log("min(0, 10) =", min(0, 10));
console.log("min(10, 0) =", min(10, 0));
console.log("min(-10, 0) =", min(-10, 0));
console.log("min(0, -10) =", min(0, -10));
console.log("min(-0, -10, -20) =", min(-0, -10, -20));
