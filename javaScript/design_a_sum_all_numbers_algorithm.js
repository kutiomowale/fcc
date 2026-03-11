#!/usr/bin/env node
function sumAll(arr) {
  let lowestNumber = arr[0] < arr[1] ? arr[0] : arr[1];
  const highestNumber = arr[0] < arr[1] ? arr[1] : arr[0];
  let result = 0;
  for (; lowestNumber <= highestNumber; lowestNumber++) {
    result += lowestNumber;
  }
  return result;
}
console.log(sumAll([4, 1]));
console.log(sumAll([5, 10]));
console.log(sumAll([10, 5]));
