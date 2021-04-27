import requests

API_KEY = ''

def intelligencehero(heroes: list, apikey: str):
    counter = 0
    max_iq = 0
    name_hero: str
    for hero in heroes:
        response = requests.get(f'https://superheroapi.com/api/{apikey}/search/{hero}')
        dict = response.json()
        if int(dict['results'][counter]['powerstats']['intelligence']) > int(max_iq):
             max_iq = dict['results'][counter]['powerstats']['intelligence']
             name_hero = dict['results'][counter]['name']

    counter += 1
    return f'Самый умный: {name_hero}'

heroes_list = ['Hulk', 'Captain America', 'Thanos']

result = intelligencehero(heroes_list, API_KEY)
print(result)