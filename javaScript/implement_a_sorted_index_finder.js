#!/usr/bin/env node
function getIndexToIns(arr, num) {
  let result;
  arr.sort((a, b) => a - b);
  result = arr.findIndex((number) => number >= num);
  return result === -1 ? arr.length : result;
}
console.log('Expecting:', 1);
console.log('Got:', getIndexToIns([1, 2, 3, 4], 1.5));
console.log('Expecting:', 2);
console.log('Got:', getIndexToIns([20, 3, 5], 19));
console.log('Expecting:', 3);
console.log('Got:', getIndexToIns([10, 20, 30, 40, 50], 35));
console.log('Expecting:', 2);
console.log('Got:', getIndexToIns([10, 20, 30, 40, 50], 30));
console.log('Expecting:', 1);
console.log('Got:', getIndexToIns([40, 60], 50));
console.log('Expecting:', 0);
console.log('Got:', getIndexToIns([3, 10, 5], 3));
console.log('Expecting:', 2);
console.log('Got:', getIndexToIns([5, 3, 20, 3], 5));
console.log('Expecting:', 2);
console.log('Got:', getIndexToIns([2, 20, 10], 19));
console.log('Expecting:', 3);
console.log('Got:', getIndexToIns([3, 10, 5], 11));
console.log('Expecting:', 0);
console.log('Got:', getIndexToIns([], 5));
