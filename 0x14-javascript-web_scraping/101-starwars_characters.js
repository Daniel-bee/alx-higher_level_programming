#!/usr/bin/node

const request = require('request');
const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + process.argv[2]
};

request(options, (error, response, body) => {
  if (error) console.log(error);
  const obj = JSON.parse(body);
  /*
  function order (url) {
    request(url, (error, response, body) => {
      if (error) console.log(error);
      const people = JSON.parse(body);
      console.log(people.url);
    });
  }
  */
  for (let i = 0; i < obj.characters.length; i++) {
    request.get(obj.characters[i], (error, response, body) => {
      if (error) console.log(error);
      const people = JSON.parse(body);
      const arr = [];
      arr.push(people);
      arr.sort(function (a, b) {
        return a.obj.characters[i] - b.people.url;
      });
      console.log(arr[0].name);
    });
  }
});
