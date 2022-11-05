import requests
import json

# Зроби виклик через API та збережи відповідь
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f'Status code: {r.status_code}')

# Дослідити структуру даних
response_dict = r.json()
readable_file = 'readable_hh_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)
