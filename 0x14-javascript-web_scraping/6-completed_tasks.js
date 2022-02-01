#!/usr/bin/node

const request = require('request');
const options = {
  url: process.argv[2]
};
request(options, (error, response, body) => {
  if (error) console.log(error);
  const obj = JSON.parse(body);
  let firstId = obj[0].userId;
  const json = {};
  function count (id) {
    let count = 0;
    for (let i = 0; i < obj.length; i++) {
      if (obj[i].completed && id === obj[i].userId) count++;
    }
    return count;
  }
  let key = '';
  key = firstId;
  json[firstId] = parseInt(count(firstId));
  for (let i = 1; i < obj.length; i++) {
    if (firstId !== obj[i].userId) {
      key = obj[i].userId;
      json[key] = parseInt(count(obj[i].userId));
      firstId = obj[i].userId;
    }
  }
  console.log(json);
});
