import requests
from pprint import pprint

def get_api_data(endpoint, params):
    try:
        re = requests.get(f"https://rickandmortyapi.com/api{endpoint}", params=params)
        return re.json() if re.status_code == 200 else None;

    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição: {e}")
        print(re.content)
        exit(1)

endpoint = get_api_data("/character/", {"name": "Rick Sanchez"})

endpoint = endpoint['results']
for character in endpoint:
    if character['name'] == "Rick Sanchez":
        pprint(character)