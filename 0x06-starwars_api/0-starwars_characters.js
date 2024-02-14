#!/usr/bin/node
//  star wars api
const request = require('request');

function makeRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      }
      resolve(JSON.parse(body));
    });
  });
}

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

async function main () {
  const result = await makeRequest(url);
  const info = result.characters;
  let character;
  for (let i = 0; i < info.length; i++) {
    character = await makeRequest(info[i]);
    console.log(character.name);
  }
}
main();
