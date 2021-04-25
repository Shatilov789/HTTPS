from pprint import pprint
import requests

class YaUploader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def upload(self):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Connect-type': 'application/json', 'Authorization': ''}
        params = {"path": self.file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        response.json()

        href = response.json().get("href", "")
        response = requests.put(href,  data=open(self.file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
           print()
           print("Success")

        return response.raise_for_status()

if __name__ == '__main__':
    uploader = YaUploader("hw_python.txt")
    result = uploader.upload()

print()
response = requests.get(f'https://superheroapi.com/api/access-token/search/batman')
data = response.json()
intelligence = []
full_name = []
list_heroes = {}
max_iq = 0

for item in data["results"]:
    for key, val in item.items():
        if "intelligence" in val:
           intelligence.append(val["intelligence"])
        elif "full-name" in val:
           full_name.append(val["full-name"])

x = 0
for _ in range(3):
    list_heroes[full_name[x]] = intelligence[x]
    x += 1

for key, val in list_heroes.items():
    if int(list_heroes[key]) > int(max_iq):
        max_iq = list_heroes[key]

for key, val in list_heroes.items():
  if list_heroes[key] == max_iq:
      print(f'Самый умный: {key}\nC IQ: {val}')