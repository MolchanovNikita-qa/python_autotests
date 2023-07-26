import requests

TOKEN = 'a45c91148c93581d7bc1754a307a2574'
BASE_URL = 'https://api.pokemonbattle.me:9104'

response_add_pokemon = requests.post(f'{BASE_URL}/pokemons', headers={'trainer_token' : TOKEN}, json={
    "name": "Vasya",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
})

print(response_add_pokemon.text)


response_change_pokemon = requests.put(f'{BASE_URL}/pokemons', headers={'trainer_token' : TOKEN}, json={
    "pokemon_id": "5320",
    "name": "Drake",
    "photo": "https://dolnikov.ru/pokemons/albums/009.png"
})

print(response_change_pokemon.text)

response_pokeball_pokemon = requests.post(f'{BASE_URL}/trainers/add_pokeball', headers={'trainer_token' : TOKEN}, json={
    "pokemon_id": "5320"
})

print(response_pokeball_pokemon.text)
