# MatrixHomeAssignment
# Pokémon API Testing

This project contains automated tests for verifying the functionality of the Pokémon API.

## Overview

The Pokémon API provides various endpoints for retrieving information about Pokémon, their types, abilities, moves, etc. This project focuses on testing the following aspects of the API:

- Verifying the response types and structure
- Checking specific Pokémon types and attributes
- Validating the weights of the heaviest Pokémon of the Fire type

## Installation

1. Clone the repository to your local machine:

    git clone https://github.com/TommyBerman/MatrixHomeAssignment.git

2. Install the required dependencies:

    pip install -r requirements.txt

## Usage

To run the tests, execute the following command:

pytest

## Test Cases

1. **test_pokemon_types**: Verifies the response from the Pokémon type API and ensures it contains exactly 20 different types.
2. **test_fire_type**: Checks if the Pokémon type API returns the correct ID for the Fire type and validates the presence of Charmander and absence of Bulbasaur in the list of Fire Pokémon.
3. **test_heaviest_fire_pokemon**: Identifies the five heaviest Pokémon of the Fire type and validates their weights against the expected values.

## Additional Details

- The tests are implemented using pytest framework with requests library for making API requests.
- Error handling is implemented to handle request exceptions and failures.
- The test report will be generated after each test run, providing details on test outcomes and any failures encountered.

##Challenges Handling
- my main challenge was in the last test, I first wanted to iterate through all of the pokemons URL endpoints and only add the fire ones, from there i could start and add each fire type weight and name to a tuple i created. However it was a range between 1 and 10278 IDs.
- The test at first took 8 minutes and failed, it was very problematic to debug.
- Instead, I have decided to go through the pokemons in the fire type endpoint, from there I implemented two helper methods, which basically iterates through the fire type responses and forwards the entry of the url to the next method, which then cultivates the name and weight of said pokemons and returns it.
- Then, the main test function calls both functions accordingly and appends it to the fire pokemon tuple.
- From there, I sorted the tuple according to the weight in descending order, took the first 5 (which should be the Heaviest), then compared it to a hard coded tuple.
- Both lists matched, Success!

## Test Report

After running the tests, you can view the detailed test report by opening the `report.html` file located in the `target` directory.

