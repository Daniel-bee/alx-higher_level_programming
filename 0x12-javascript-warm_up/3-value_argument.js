#!/usr/bin/node

const args = process.argv;
let count;

args.forEach((val, index) => {
  count = index;
});

if (count === 1) {
  console.log('No argument');
} else {
  for (let i = 2; i <= count; i++) {
    console.log(args[i]);
  }
}
