#!/usr/bin/node

const request = require('request');
const options = {
  url: process.argv[2],
  method: 'GET'
};
request(options, (error, response, body) => {
  if (error) console.log(error);
  const obj = JSON.parse(body);
  let firstId = obj[0].userId;
  let json = {};
  function count (id) {
    let count = 0;
    for (let i = 0; i < obj.length; i++) {
      if (obj[i].completed && id === obj[i].userId) count++;
    }
    return count;
  }
  json[firstId] = count(firstId);
  for (let i = 1; i < obj.length; i++) {
    if (firstId !== obj[i].userId) {
      json[obj[i].userId] = count(obj[i].userId);
      firstId = obj[i].userId;
    }
  }
  json = JSON.stringify(json)
  console.log(json);
});
