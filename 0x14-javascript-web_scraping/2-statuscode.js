#!/usr/bin/node

const request = require('require');
const URL = process.argv[2];

request(URL, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
