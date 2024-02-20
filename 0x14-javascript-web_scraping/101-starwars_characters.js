#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

printFilmCharacters(url);

function printFilmCharacters (filmUrl) {
  request(filmUrl, function (error, response, body) {
    if (!error) {
      const characters = JSON.parse(body).characters;
      printCharacterNames(characters, 0);
    }
});
}

function printCharacterNames (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharacterNames(characters, index + 1);
      }
    }
  });
}
