#!/usr/bin/env node
//console.log(square3(5));
function square(number) {
  return number * number;
}
const square2 = function(number) {
  return number * number;
};
const square3 = number => number * number;
console.log(square3(5));
