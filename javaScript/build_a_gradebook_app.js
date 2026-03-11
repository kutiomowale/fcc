#!/usr/bin/env node
function getAverage(scores) {
  let totalScores = 0;
  let numberOfScores = 0;
  for (const score of scores) {
    totalScores += score;
    numberOfScores += 1;
  }
  return totalScores / numberOfScores;
}

function getGrade(score) {
  if (score === 100) {return 'A+';}
  if (score >= 90 && score <= 99) {return 'A';}
  if (score >= 80 && score <= 89) {return 'B';}
  if (score >= 70 && score <= 79) {return 'C';}
  if (score >= 60 && score <= 69) {return 'D';}
  if (score >= 0 && score <= 59) {return 'F';}
}

function hasPassingGrade(score) {return getGrade(score) !== 'F';}

function studentMsg(scores, score) {
  if (hasPassingGrade(score)) {
    return `Class average: ${getAverage(scores)}. Your grade: ${getGrade(score)}. You passed the course.`;
  }
  return `Class average: ${getAverage(scores)}. Your grade: ${getGrade(score)}. You failed the course.`;
}

console.log(getAverage([2, 3]));
console.log(100, getGrade(100), hasPassingGrade(100) ? 'Passed': 'Failed');
console.log(92, getGrade(92), hasPassingGrade(92) ? 'Passed': 'Failed');
console.log(85, getGrade(85), hasPassingGrade(85) ? 'Passed': 'Failed');
console.log(70, getGrade(70), hasPassingGrade(70) ? 'Passed': 'Failed');
console.log(68, getGrade(68), hasPassingGrade(68) ? 'Passed': 'Failed');
console.log(53, getGrade(53), hasPassingGrade(53) ? 'Passed': 'Failed');

console.log(studentMsg([92, 88, 12, 77, 57, 100, 67, 38, 97, 89], 37));
console.log(studentMsg([56, 23, 89, 42, 75, 11, 68, 34, 91, 19], 100));
console.log(studentMsg([92, 88, 12, 77, 57, 100, 67, 38, 97, 89], 37));
