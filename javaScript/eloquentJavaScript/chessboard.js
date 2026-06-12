#!/usr/bin/env node
const size = 100;
let i = 0, j = 0, chessboard = "";
while (i < size) {
  j = 0;
  while (j < size) {
    if ((i + j) % 2  == 0) chessboard += " ";
    else chessboard += "#";
    j++;
  }
  chessboard += "\n";
  i++;
}
console.log(chessboard);
