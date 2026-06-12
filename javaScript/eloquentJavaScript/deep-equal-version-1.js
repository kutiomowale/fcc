#!/usr/bin/env node
const obj1 = {one: 1, two: 2, three: 3};
const obj2 = {two: 2, one: 1, three: 3};
const obj3 = {one: 1, two: 5, three: 3};
console.log(deepEqual(obj1, obj2));
console.log(deepEqual(obj1, obj3));
console.log(deepEqual(obj2, obj3));
function deepEqual(a, b) {
  const aKeys = Object.keys(a);
  const bKeys = Object.keys(b);
  if (aKeys.length != bKeys.length) {
    return false;
  }
  for (const key of aKeys) {
    if (!bKeys.includes(key)) {
      return false;
    } else if (a[key] !== b[key]) {
      return false;
    }
  }
  return true;
}
