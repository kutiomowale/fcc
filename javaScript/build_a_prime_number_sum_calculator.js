#!/usr/bin/env node
function generatePrimes(limit) {
  // Code for generatePrimes was generated with the use of Ai
  const seive = new Array(limit + 1).fill(true);
  seive[0] = seive[1] = false;

  for (let i = 2; i * i <= limit; i++) {
    if (seive[i]) {
      for (let j = i * i; j <= limit; j += i) {
        seive[j] = false;
      }
    }
  }

  return seive.map((isPrime, index) => isPrime ? index : null).filter(n => n !== null);
}

function sumPrimes(num) {
  if (num < 2) {
    return 0;
  }
  return generatePrimes(num).reduce((accu, num) => accu + num, 0);
}

console.log(sumPrimes(10));
console.log(sumPrimes(5));
console.log(sumPrimes(2));
console.log(sumPrimes(0));
console.log(sumPrimes(977));

const primes41 = generatePrimes(41);
console.log(`Primes up to 41:\n${primes41}`);
