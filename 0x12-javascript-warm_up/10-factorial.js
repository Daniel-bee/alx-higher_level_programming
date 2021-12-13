#!/usr/bin/node

function factorial (x) {
  const number = parseInt(x);
  if (isNaN(number)) {
    return 1;
  }
  if (x === 0) {
    return 1;
  }
  return x * factorial(number - 1);
}
console.log(factorial(process.argv[2]));
