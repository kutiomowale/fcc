#!/usr/bin/env node
function arrayToList(array) {
  let list = null;
  for (let i = array.length - 1; i >= 0; i--) {
    list = {value: array[i], rest: list};
  }
  return list;
}

// listToArray - a function that produces an array from a list.
function listToArray(list) {
  const array = [];
  for (node = list; node; node = node.rest) {
    array.push(node.value);
  }
  return array;
}

// prepend - A helper function which takes an element and a list
// and creates a new list that adds the element to the front of the input list.
function prepend(value, list) {
  return {value, rest: list};
}

// nth - a function which takes a list and a number and returns the
// element at the given position in the list
// (with zero referring to the first element)
// or undefined when there is no such element.
function nth(list, n) {
  for (let position = 0, node = list; node; position++, node = node.rest) {
    if (position === n) return node.value;
  }
  return undefined;
}
// If you haven’t already, also write a recursive version of nth.
function nthRecursive(list, n) {
  if (!list) return undefined;
  else if (n === 0) return list.value;
  else return nthRecursive(list.rest, n - 1);
}

console.log(arrayToList([10, 20]));
// → {value: 10, rest: {value: 20, rest: null}}
console.log(listToArray(arrayToList([10, 20, 30])));
// → [10, 20, 30]
console.log(prepend(10, prepend(20, null)));
// → {value: 10, rest: {value: 20, rest: null}}
console.log(nth(arrayToList([10, 20, 30]), 1));
// → 20
