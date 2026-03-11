#!/usr/bin/env node
function hcf(a, b) {
  let small, big, remainder;
  small = a < b ? a : b;
  big = a < b ? b : a;
  remainder = big % small;
  while (remainder) {
    big = small;
    small = remainder;
    remainder = big % small;
  }
  return small;
}
function lcm(a, b) {
  return (a * b) / hcf(a, b);

}
function func(arr) {
  let small, big, range;

  small = arr[0] < arr[1] ? arr[0] : arr[1];
  big = arr[0] < arr[1] ? arr[1] : arr[0];

  range = [];
  for (let i = small; i <= big; i++) {range.push(i);}

  return range.reduce((acc, num) => lcm(acc, num));
}

console.log(func([23, 18]));
console.log(func([18, 23]));
console.log(hcf(23, 18));
