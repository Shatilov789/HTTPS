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