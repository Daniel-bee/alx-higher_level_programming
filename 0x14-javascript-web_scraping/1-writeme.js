#!/usr/bin/node

const fs = require('fs');
/*
script that writes a string to a file
process.argv[2] -> file name
process.argv[3] -> file content
*/
fs.writeFile(process.argv[2], process.argv[3] + '\n', 'utf-8', err => {
  if (err) {
    console.error(err);
  }
});
