#!/usr/bin/env node
const obj1 = {one: 1, two: 2, three: 3};
const obj2 = {two: 2, one: 1, three: 3};
const obj3 = {one: 1, two: 5, three: 3};
console.log(deepEqual(obj1, obj2));
console.log(deepEqual(obj1, obj3));
console.log(deepEqual(obj2, obj3));
function deepEqual(a, b) {
  if (a === null || b === null) return a === b;
  else if (typeof a == "object" && typeof b == "object") {
    const aKeys = Object.keys(a);
    const bKeys = Object.keys(b);
    if (aKeys.length != bKeys.length) {
      return false;
    }
    for (const key of aKeys) {
      if (!bKeys.includes(key)) {
        return false;
      } else if (!deepEqual(a[key], b[key])) {
        return false;
      }
    }
    return true;
  }
  else return a === b;
}

console.log("\n*******\n");
let obj = {here: {is: "an"}, object: 2};
console.log(deepEqual(obj, obj));
// → true
console.log(deepEqual(obj, {here: 1, object: 2}));
// → false
console.log(deepEqual(obj, {here: {is: "an"}, object: 2}));
// → true
