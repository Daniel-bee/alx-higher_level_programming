#!/usr/bin/node

const request = require('request');
const options = {
  url: process.argv[2] + '/18/',
  method: 'GET'
};

request(options, (error, response, body) => {
  if (error) console.log(error);
  console.log(body.length);
});
