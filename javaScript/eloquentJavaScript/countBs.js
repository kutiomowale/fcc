#!/usr/bin/env node
// A function called countBs that takes a string as its only argument
// and returns a number that indicates how many uppercase B characters
// there are in the string.
function countBs(aString) {
  return countChars(aString, 'B');
}

console.log("countBs('abcBg') =", countBs("abcBg"));
console.log("countBs('a') =", countBs("a"));
console.log("countBs('') =", countBs(""));
console.log("countBs('Ɓ') =", countBs("Ɓ"));

function countChars(aString, c) {
  //find how many c's are in string astring. c can be any charactwr.
  let counter = 0;
  for (let i = 0; i < aString.length; i++) {
    if (aString[i] === c) {
      counter++;
    }
  }
  return counter; 
}

console.log("countChars('abcd', 'a') =", countChars('abcd', 'a'));
console.log("countChars('abcAdA', 'A') =", countChars('abcAdA', 'A'));
