#!/usr/bin/env node
function uniteUnique(...arrays) {
  const result = [];
  for (const array of arrays) {
    for (const element of array) {
      if (!result.includes(element)) {
        result.push(element);
      }
    }
  }
  return result;
}

console.log('uniteUnique([1, 3, 2], [5, 2, 1, 4], [2, 1]) should return:\n[1, 3, 2, 5, 4]');
console.log();
console.log(uniteUnique([1, 3, 2], [5, 2, 1, 4], [2, 1]));
