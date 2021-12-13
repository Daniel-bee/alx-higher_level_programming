#!/usr/bin/node

if (process.argv.length < 4) {
  console.log('0');
} else {
  const big = process.argv.slice(2);

  big.sort((x, y) => y - x);
  console.log(big[1]);
}
