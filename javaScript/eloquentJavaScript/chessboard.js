#!/usr/bin/env node
//8x8 grid
const line = "# ".repeat(4) + "\n";
let chessboard = "";
for (let lineNumber = 0; lineNumber < 8; lineNumber++) {
  if (lineNumber % 2 == 0) chessboard += (" " + line);
  else chessboard += line;
}

console.log(chessboard);
