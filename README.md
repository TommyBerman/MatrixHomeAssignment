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

## Test Report

After running the tests, you can view the detailed test report by opening the `report.html` file located in the `target` directory.

