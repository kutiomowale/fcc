#!/usr/bin/env node
function chunkArrayInGroups(arr, size) {
  const arrCopy = [...arr];
  const result = [];
  while (arrCopy.length > 0) {
    result.push(arrCopy.splice(0, size));
  }
  return result;
}
console.log(chunkArrayInGroups(['a', 'b', 'c', 'd'], 2));
console.log(chunkArrayInGroups([0, 1, 2, 3, 4, 5], 3));
console.log(chunkArrayInGroups([0, 1, 2, 3, 4, 5], 2));
console.log(chunkArrayInGroups([0, 1, 2, 3, 4, 5], 4));
console.log(chunkArrayInGroups([0, 1, 2, 3, 4, 5, 6], 3));
console.log(chunkArrayInGroups([0, 1, 2, 3, 4, 5, 6, 7, 8], 4));
console.log(chunkArrayInGroups([0, 1, 2, 3, 4, 5, 6, 7, 8], 2));
/*
 * create an empty array
 * pop size number of elements from arr to new sub array
 * add the new sub array to the result
 * do this again as long as there are elements left to remove
 *
 *
 *
 *
 *
 */

