#!/usr/bin/env node
// [1, 2, 3 ]
function arrayToList(array) {
  const list = {};
  if (array.length === 0) return list;
  let temp = list, prev;
  for (const element of array) {
    temp.value = element;
    temp.rest = {};
    prev = temp;
    temp = temp.rest;
  }
  prev.rest = null;
  return list;
}

console.log(arrayToList([1, 2, 3]));
console.log(arrayToList([]));
