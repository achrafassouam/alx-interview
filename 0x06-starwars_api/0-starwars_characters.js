#!/usr/bin/node

// Import the 'request' module to make HTTP requests
const request = require('request');

// Get the film ID from the command line arguments
const filmId = process.argv[2];

// Construct the API URL for the specified film
const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

/**
 * Makes an HTTP request to the Star Wars API to retrieve information about a specific film.
 * Then, for each character in the film, another request is made to retrieve and print the character's name.
 *
 * @param {string} url - The URL of the Star Wars API endpoint for the specified film.
 */
request(url, async (err, response, body) => {
  if (err) {
    // Print any errors encountered during the request
    console.log(err);
  }

  // Parse the response body to extract the list of character URLs
  const characters = JSON.parse(body).characters;

  // Iterate over each character URL and retrieve the character's name
  for (const characterId of characters) {
    // Use a Promise to handle asynchronous requests
    await new Promise((resolve, reject) => {
      request(characterId, (err, response, body) => {
        if (err) {
          // Reject the Promise if an error occurs
          reject(err);
        }
        // Print the character's name
        console.log(JSON.parse(body).name);
        // Resolve the Promise after the request completes
        resolve();
      });
    });
  }
});
