#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], (error, response) => {
  if (error) {
    console.log('Error:', error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
