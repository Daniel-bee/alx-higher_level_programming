#!/usr/bin/node

const request = require('request');
const options = {
  url: process.argv[2],
  method: 'GET'
};

request(options, (error, response, body) => {
  if (error) console.log(error);
  let count = 0;
  obj = JSON.parse(body);
  for (let j = 0; j < obj.results.length ;j++) {
    const len = obj.results[j].characters.length;
    for (let i = 0; i < len; i++) {
      if (obj.results[j].characters[i] === 'https://swapi-api.hbtn.io/api/people/18/') count += 1;
    }
  }
  console.log(`${count}`);
});
