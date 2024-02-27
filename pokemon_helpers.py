import requests


# Function to handle errors
def handle_error(exception):
    print(f"An error occurred: {exception}")


# Function to get URLs of fire-type Pokémon
def get_fire_pokemon_urls(base_url, fire_type_id):
    # Set default fire type ID if not provided
    if fire_type_id is None:
        fire_type_id = 10

    # Construct URL for fire type endpoint
    fire_type_url = f"{base_url}/type/{fire_type_id}"

    # Send GET request to fire type endpoint
    response = requests.get(fire_type_url)

    # Check if request was successful
    if response.status_code == 200:
        data = response.json()
        # Extract URLs of fire-type Pokémon
        return [entry['pokemon']['url'] for entry in data['pokemon']]
    else:
        # Raise exception if request failed
        raise requests.exceptions.RequestException("Failed to fetch fire type Pokemon URLs")


# Function to fetch data for a Pokémon
def fetch_pokemon_data(url):
    # Send GET request to Pokémon URL
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        pokemon_data = response.json()
        # Extract name and weight of Pokémon
        name = pokemon_data['name']
        weight = pokemon_data['weight']
        return name, weight
    else:
        # Raise exception if request failed
        raise requests.exceptions.RequestException(f"Failed to fetch data for Pokemon at URL: {url}")
