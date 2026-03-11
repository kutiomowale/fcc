#!/usr/bin/env node
function pyramid(pattern, noOfRows, shouldFaceDown) {
  function pyramidUp(pattern, noOfRows) {
    const base = (2 * noOfRows) - 1;
    let result = '\n';
    for (let i = 1; i <= noOfRows; i++) {
      const level = (2 * i) - 1;
      const padLeft = Math.floor((base - level) / 2);
      result += ' '.repeat(padLeft) + pattern.repeat(level) + '\n';
    }
    return result;
  }
  function pyramidDown(pattern, noOfRows) {
    const base = (2 * noOfRows) - 1;
    let result = '\n';
    for (let i = noOfRows; i >= 1; i--) {
      const level = (2 * i) - 1;
      const padLeft = Math.floor((base - level) / 2);
      result += ' '.repeat(padLeft) + pattern.repeat(level) + '\n';
    }
    return result;
  }
  if (shouldFaceDown) {
    return pyramidDown(pattern, noOfRows);
  } else {
    return pyramidUp(pattern, noOfRows);
  }
}

for (let i = 0; i < 11; i++) {
  console.log(pyramid('o', i, false));
}
for (let i = 0; i < 11; i++) {
  console.log(pyramid('o', i, true));
}
