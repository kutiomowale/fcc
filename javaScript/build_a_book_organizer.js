#!/usr/bin/env node
const books = [
  {
    title: 'Book1',
    authorName: 'Book1Author',
    releaseYear: 1900
  },
  {
    title: 'Book2',
    authorName: 'Book2Author',
    releaseYear: 1940
  },
  {
    title: 'Book3',
    authorName: 'Book3Author',
    releaseYear: 1950
  },
  {
    title: 'Book4',
    authorName: 'Book4Author',
    releaseYear: 1980
  },
  {
    title: 'Book5',
    authorName: 'Book5Author',
    releaseYear: 2020
  }
];

function sortByYear(booka, bookb) {
  if (booka.releaseYear < bookb.releaseYear) {
    return (-1);
  } else if (booka.releaseYear > bookb.releaseYear) {
    return (1);
  } else if (booka.releaseYear === bookb.releaseYear) {
    return (0);
  }
}

console.log('\nAll books:');
console.log(books.map((book) => `${book.title} by ${book.author}. ${book.releaseYear}`).join('\n'));

const filterYear = 1950;
const filteredBooks = books.filter((book) => book.releaseYear <= filterYear);
filteredBooks.sort(sortByYear);
console.log(`\nAll books written on or before ${filterYear}:`);
console.log(filteredBooks.map((book) => `${book.title} by ${book.author}. ${book.releaseYear}`).join('\n'));
