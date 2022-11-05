import requests
import json

headers = {'Accept': 'application/vnd.github.v3+json'}
p_language = 'Java'
url = f'https://api.github.com/search/repositories?q=language:{p_language}'
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
response_dict = r.json()
total_count = response_dict['total_count']

file_name = f'{p_language}.json'
with open(file_name, 'w') as f:
    json.dump(response_dict, f)
