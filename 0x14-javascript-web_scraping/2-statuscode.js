#!/usr/bin/node

const request = require('request');
/*
const options = {
  url: process.argv[2],
  method: 'GET'
};
*/
request(process.argv[2], (error, response, body) => {
  if (error) console.log(error);
  console.log('Code:', response.statusCode);
});
