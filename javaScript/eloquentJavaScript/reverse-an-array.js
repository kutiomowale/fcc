#!/usr/bin/env node
// reverseArray - this function takes an array as its argument and
// produces a new array that has the same elements in the inverse order.
function reverseArray(array) {
  const arrayReversed = [];
  for (let index = array.length - 1; index >= 0; index--) {
    arrayReversed.push(array[index]);
  }
  return arrayReversed;
}
const myArray = [1, 2, 3, 4, 5];
console.log(myArray);
console.log(reverseArray(myArray));
console.log(myArray);

// reverseArrayInPlace - this function modify the array given as its
// argument by reversing its elements.
function reverseArrayInPlace(array) {
  let i, j, temp;
  i = 0;
  j = array.length - 1;
  for (; i < j; i++, j--) {
    temp = array[i];
    array[i] = array[j];
    array[j] = temp;
  }
}

const mySecondArray = [0, 1];
console.log();
console.log(mySecondArray);
reverseArrayInPlace(mySecondArray);
console.log(mySecondArray);
