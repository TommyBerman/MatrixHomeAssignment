import pytest
import requests
from pokemon_helpers import get_fire_pokemon_urls, fetch_pokemon_data, handle_error


@pytest.fixture
def base_url():
    return "https://pokeapi.co/api/v2"


fire_type_id = None


def test_pokemon_types(base_url):
    try:
        response = requests.get(base_url + "/type")

        assert response.status_code == 200

        assert 'application/json' in response.headers['Content-Type']

        data = response.json()

        assert len(data['results']) == 20

        print("Test Passed: Pokemon type API returned a response with type ", response.headers['Content-Type'],
              " and exactly ", len(data['results']), " different pokemon types.")
    except requests.exceptions.HTTPError as e:
        handle_error(e)
    except requests.exceptions.RequestException as e:
        handle_error(e)


def test_fire_type(base_url):
    global fire_type_id
    try:
        response = requests.get(base_url + "/type")
        data = response.json()['results']
        for pokeType in data:
            if 'name' in pokeType and pokeType['name'] == 'fire':
                print("Found desired type: ", pokeType['name'])
                fire_type_id = pokeType['url'].split('/')[-2]
                print("ID: ", fire_type_id)
                break
        else:
            pytest.fail("Desired type 'fire' not found in the response")
        fire_type_response = requests.get(base_url + f"/type/{fire_type_id}")
        fire_type_data = fire_type_response.json()['pokemon']

        charmander_found = False
        for pokemon in fire_type_data:
            if 'name' in pokemon['pokemon'] and pokemon['pokemon']['name'] == 'charmander':
                charmander_found = True
                break
        assert charmander_found, "Charmander not found in the list of Pokémon for the 'fire' type"
        print("Test passed: Charmander is in the list of Pokémon for the 'fire' type.")

        bulbasaur_found = False
        for pokemon in fire_type_data:
            if 'name' in pokemon['pokemon'] and pokemon['pokemon']['name'] == 'bulbasaur':
                bulbasaur_found = True
            break
        assert not bulbasaur_found, "Bulbasaur  a 'water' type was found in the list of Pokémon for the 'fire' type"
        print("Test passed: Bulbasaur is not in the list of Pokémon for the 'fire' type.")

    except requests.exceptions.HTTPError as e:
        handle_error(e)
    except requests.exceptions.RequestException as e:
        handle_error(e)


def test_heaviest_fire_pokemon(base_url):
    try:
        fire_pokemon_urls = get_fire_pokemon_urls(base_url, fire_type_id)
        fire_pokemon_info = []

        for url in fire_pokemon_urls:
            name, weight = fetch_pokemon_data(url)
            if name and weight:
                fire_pokemon_info.append((name, weight))

        fire_pokemon_info.sort(key=lambda x: x[1], reverse=True)

        expected_pokemon_info = [
            ('charizard-gmax', 10000),
            ('cinderace-gmax', 10000),
            ('coalossal-gmax', 10000),
            ('centiskorch-gmax', 10000),
            ('groudon-primal', 9997)
        ]

        for i in range(5):
            assert expected_pokemon_info[i] == fire_pokemon_info[i]
            print("Expected pokemon info:", expected_pokemon_info[i], "Actual pokemon info:", fire_pokemon_info[i])
        print("Test passed: Verified the weights of the five heaviest Pokémon of the Fire type.")

    except requests.exceptions.HTTPError as e:
        handle_error(e)

    except requests.exceptions.RequestException as e:
        handle_error(e)
