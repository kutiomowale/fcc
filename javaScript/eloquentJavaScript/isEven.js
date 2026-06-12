#!/usr/bin/env node
//max safe value for call stack on my termux on tecno pop 7 for this function: 36514
function isEven(positiveWholeNumber) {
  if (positiveWholeNumber === 0) return true;
  else if (positiveWholeNumber === 1 || positiveWholeNumber < 0) return false;
  else return isEven(positiveWholeNumber - 2);
}
console.log(isEven(-1));
