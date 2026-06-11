#!/usr/bin/env node
const array = [1, 2, 3, 4, 5];
console.log("array:", array);
for (let temp, i = 0, j = array.length - 1; i < j; i++, j--) {
  temp = array[i];
  console.log("temp:", temp);
  array[i] = array[j];
  console.log("array[i]:", array[i]);
  array[j] = temp;
  console.log("array[j]:", array[j]);
}
console.log("array:", array);
