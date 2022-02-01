#!/usr/bin/node

const request = require('request');
const options = {
  url: process.argv[2],
  method: 'GET'
};
request(options, (error, response, body) => {
  if (error) console.log(error);
  const obj = JSON.parse(body);
  function count (userid) {
    let count = 0;
    for (let j = 0; j < obj.length; j++) {
      if (obj[j].userId === userid) {
        if (obj[j].completed) count++;
      }
    }
    return count;
  }
  const jsonData = {};
  for (let i = 1; i < 11; i++) {
    jsonData[i] = count(i);
  }
  console.log(jsonData);
});
