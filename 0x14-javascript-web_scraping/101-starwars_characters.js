#!/usr/bin/node

const request = require('request');
const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + process.argv[2],
  method: 'GET'
};

request(options, (error, response, body) => {
  if (error) console.log(error);
  const obj = JSON.parse(body);
  function order (url) {
    request(url, (error, response, body) => {
      if (error) console.log(error);
      const people = JSON.parse(body);
      console.log(people.name);
    });
  }
  let url = "";
  for (let i = 0; i < obj.characters.length; i++) {
    url = obj.characters[i];
    order(url);
  }
});
