#!/usr/bin/env node
const questions = [
  {category: '1. The Big Three Statements',
    question: '1. Which financial statement shows a company’s revenues, expenses, and net income over a period?',
    choices: ['a) Balance Sheet', 'b) Income Statement', 'c) Cash Flow Statement'],
    answer: 'b) Income Statement'},
  {category: '2. Assets & Liabilities: The Balance Sheet Game',
    question: '2. Which of these is an example of a liability?',
    choices: ['a) Cash in the bank', 'b) Office equipment', 'c) Money owed to suppliers'],
    answer: 'c) Money owed to suppliers'},
  {category: '3. Accrual vs. Cash: The Timing Challenge',
    question: '3. Under the accrual basis of accounting, when is revenue recorded?',
    choices: ['a) When cash is actually received', 'b) When the customer places an order', 'c) When the service is performed or goods are delivered'],
    answer: 'c) When the service is performed or goods are delivered'},
  {category: '4. The Accounting Equation: Balance It!',
    question: '4. What is the correct formula for the accounting equation?',
    choices: ['a) Assets = Liabilities – Equity', 'b) Assets = Liabilities + Equity', 'c) Equity = Assets + Liabilities'],
    answer: 'b) Assets = Liabilities + Equity'},
  {category: '5. Debits & Credits: The Double-Entry Dance',
    question: '5. Which account increases with a debit?',
    choices: ['a) Accounts Payable', 'b) Common Stock', 'c) Accounts Receivable'],
    answer: 'c) Accounts Receivable'}
];

function getRandomQuestion(arrayOfQuestions) {
  return arrayOfQuestions[Math.floor(Math.random() * arrayOfQuestions.length)];
}

function getRandomComputerChoice(arrayOfChoices) {
  return arrayOfChoices[Math.floor(Math.random() * arrayOfChoices.length)];
}

function getResults(question, computersRandomChoice) {
  return computersRandomChoice === question.answer ? 'The computer\'s choice is correct!' : `The computer's choice is wrong. The correct answer is: ${question.answer}`;
}

const randomQuestion = getRandomQuestion(questions);
console.log('**********');
console.log('Random Question:');
console.log(randomQuestion.question);
console.log(randomQuestion.choices[0]);
console.log(randomQuestion.choices[1]);
console.log(randomQuestion.choices[2]);
console.log();
console.log('Computer\'s choice:');
const compRandomChoice = getRandomComputerChoice(randomQuestion.choices);
console.log(compRandomChoice);
console.log();
console.log(getResults(randomQuestion, compRandomChoice));
console.log('**********');
