#!/usr/bin/env node
// range - a function that takes two arguments, start and end,
// and returns an array containing all the numbers from start up to
// and including end.
// It can take an optional third argument that indicates the “step”
// value used when building the array. If no step is given,
// the elements should go up by increments of one.
function range(start, end, step = 1) {
  const rangeArray = [];
  step = start > end && step === 1 ? -1: step; 
  if (step >= 1)
    for (; start <= end; start += step) rangeArray.push(start);
  else if (step < 0)
    for (; start >= end; start += step) rangeArray.push(start);
  return rangeArray;
}

console.log(range(1, 10));
console.log(range(0, 5));
console.log(range(-10, -5));
console.log(range(1, 10, 2));
console.log(range(5, 2, -1));
console.log(range(5, 2, -1));
console.log("******", range(2, 5, -1));
console.log("******", range(5, 2));
console.log("******", range(1, 3, 0));

// sum - a function that takes an array of numbers
// and returns the sum of these numbers.
function sum(numbers) {
  let sumNumbers = 0;
  for (const number of numbers) sumNumbers += number;
  return sumNumbers;
}
console.log(sum(range(1, 10)));
console.log(sum(range(0, 5)));
