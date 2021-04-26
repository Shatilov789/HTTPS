from pprint import pprint
import requests
response = requests.get(f'https://superheroapi.com/api/2619421814940190/search/batman')
dict = response.json()

def intelligence_hero(dict):
    counter = 0
    max_iq = 0
    name_hero: str
    id_hero: str

    for _ in range(3):
       if int(dict['results'][counter]['powerstats']['intelligence']) > int(max_iq):
            max_iq = dict['results'][counter]['powerstats']['intelligence']
            name_hero = dict['results'][counter]['name']
            id_hero = dict['results'][counter]['id']
       counter += 1
    print()
    print(f'ID: {id_hero} - Самый умный персонаж "{name_hero}" c IQ:{max_iq}')

intelligence_hero(dict)
