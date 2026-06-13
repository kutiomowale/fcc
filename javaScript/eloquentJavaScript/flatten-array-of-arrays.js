#!/usr/bin/env node
const arrays = [[0, 1, 2], [3], [4, 5]];
console.log(arrays);
function flatten(arrayOfArrays) {
  return arrayOfArrays.reduce((a, b) => a.concat(b), []);
}
console.log(flatten(arrays));
console.log(arrays);
