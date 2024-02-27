import pytest
import requests
from pokemon_helpers import get_fire_pokemon_urls, fetch_pokemon_data, handle_error


@pytest.fixture
def base_url():
    return "https://pokeapi.co/api/v2"


fire_type_id = None


def test_pokemon_types(base_url):
    try:
        # Send a request to get Pokémon types
        response = requests.get(f"{base_url}/type")

        # Check if the response status code is 200 (OK)
        assert response.status_code == 200

        # Check if the response content type is JSON
        assert 'application/json' in response.headers['Content-Type']

        # Convert the response JSON data to a Python dictionary
        data = response.json()

        # Check if there are exactly 20 different Pokémon types in the response
        assert len(data['results']) == 20

        # Print a success message if all checks pass
        print("Test Passed: Pokemon type API returned a response with type ", response.headers['Content-Type'],
              " and exactly ", len(data['results']), " different pokemon types.")
    except requests.exceptions.HTTPError as e:
        # Handle HTTP errors
        handle_error(e)
    except requests.exceptions.RequestException as e:
        # Handle other request exceptions
        handle_error(e)


def test_fire_type(base_url):
    global fire_type_id
    try:
        # Send a request to get Pokémon types
        response = requests.get(f"{base_url}/type")
        data = response.json()['results']
        for pokeType in data:
            # Check if the desired type 'fire' is found
            if 'name' in pokeType and pokeType['name'] == 'fire':
                print("Found desired type: ", pokeType['name'])
                # Split the url by '/' and assign the second before last item to fire_type_id
                fire_type_id = pokeType['url'].split('/')[-2]
                print("ID: ", fire_type_id)
                break
        else:
            # Fail the test if 'fire' type is not found in the response
            pytest.fail("Desired type 'fire' not found in the response")
        # Get detailed information about the 'fire' type
        fire_type_response = requests.get(f"{base_url}/type/{fire_type_id}")
        fire_type_data = fire_type_response.json()['pokemon']

        # Check if Charmander is in the list of Pokémon for the 'fire' type
        charmander_found = False
        for pokemon in fire_type_data:
            if 'name' in pokemon['pokemon'] and pokemon['pokemon']['name'] == 'charmander':
                charmander_found = True
                break
        assert charmander_found, "Charmander not found in the list of Pokémon for the 'fire' type"
        print("Test passed: Charmander is in the list of Pokémon for the 'fire' type.")

        # Check if Bulbasaur is not in the list of Pokémon for the 'fire' type
        bulbasaur_found = False
        for pokemon in fire_type_data:
            if 'name' in pokemon['pokemon'] and pokemon['pokemon']['name'] == 'bulbasaur':
                bulbasaur_found = True
            break
        assert not bulbasaur_found, "Bulbasaur  a 'water' type was found in the list of Pokémon for the 'fire' type"
        print("Test passed: Bulbasaur is not in the list of Pokémon for the 'fire' type.")

    except requests.exceptions.HTTPError as e:
        # Handle HTTP errors
        handle_error(e)
    except requests.exceptions.RequestException as e:
        # Handle other request exceptions
        handle_error(e)


def test_heaviest_fire_pokemon(base_url):
    try:
        # Get the URLs of fire type Pokémon
        fire_pokemon_urls = get_fire_pokemon_urls(base_url, fire_type_id)
        fire_pokemon_info = []

        # Iterate through each Pokémon URL
        for url in fire_pokemon_urls:
            name, weight = fetch_pokemon_data(url)
            if name and weight:
                fire_pokemon_info.append((name, weight))

        # Sort the Pokémon info by weight in descending order
        fire_pokemon_info.sort(key=lambda x: x[1], reverse=True)

        # Define the expected Pokémon info with their weights
        expected_pokemon_info = [
            ('charizard-gmax', 10000),
            ('cinderace-gmax', 10000),
            ('coalossal-gmax', 10000),
            ('centiskorch-gmax', 10000),
            ('groudon-primal', 9997)
        ]

        # Compare the actual and expected Pokémon info
        for i in range(5):
            assert expected_pokemon_info[i] == fire_pokemon_info[i]
            # Print the expected and actual Pokémon info for verification
            print("Expected pokemon info:", expected_pokemon_info[i], "Actual pokemon info:", fire_pokemon_info[i])
        # Print a message indicating the test passed
        print("Test passed: Verified the weights of the five heaviest Pokémon of the Fire type.")

    except requests.exceptions.HTTPError as e:
        # Handle HTTP errors
        handle_error(e)

    except requests.exceptions.RequestException as e:
        # Handle other request exceptions
        handle_error(e)
