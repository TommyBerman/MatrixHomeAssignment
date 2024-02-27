import requests


def handle_error(exception):
    print(f"An error occurred: {exception}")


def get_fire_pokemon_urls(base_url, fire_type_id):
    if fire_type_id is None:
        fire_type_id = 10

    fire_type_url = f"{base_url}/type/{fire_type_id}"
    response = requests.get(fire_type_url)
    if response.status_code == 200:
        data = response.json()
        return [entry['pokemon']['url'] for entry in data['pokemon']]
    else:
        raise requests.exceptions.RequestException("Failed to fetch fire type Pokemon URLs")


def fetch_pokemon_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        name = pokemon_data['name']
        weight = pokemon_data['weight']
        return name, weight
    else:
        raise requests.exceptions.RequestException(f"Failed to fetch data for Pokemon at URL: {url}")
