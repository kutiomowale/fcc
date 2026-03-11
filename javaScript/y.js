#!/usr/bin/env node
function steamrollArray(arr) {
  return arr.reduce((acc, curr) => {
    if (Array.isArray(curr)) {
      acc.push(...steamrollArray(curr));
      return acc;
    } else {
      acc.push(curr);
      return acc;
    }
  }, []);
}

console.log(steamrollArray([[['a']], [['b']]]));
