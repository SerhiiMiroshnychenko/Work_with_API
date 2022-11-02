import requests

# Зробити виклик через API та зберегти відповідь
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'  # Зберігаємо URL
# виклику через API у змінну
headers = {'Accept': 'application/vnd.github.v3+json'}  # Зазначаємо версію API,
# що використовується на сайті; тут третя.
r = requests.get(url, headers=headers)  # Робимо запит
print(f"Status code: {r.status_code}")  # Атрибут status_code повідомляє нам, чи був запит успішним
# (статус 200 --> успішно)

# Зберегти відповідь API у змінну
response_dict = r.json()

# Обробити результати
print(response_dict.keys())
