import requests
import pytest

BASE_URL = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(f'{BASE_URL}/trainers')
    assert response.status_code == 200

def test_name():
    response = requests.get(f'{BASE_URL}/trainers', params={'trainer_id' : 1388})
    assert response.json()['trainer_name'] == 'Neket'
    
    

