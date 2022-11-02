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
print(f"Total repositories: {response_dict['total_count']}")  # Загальна кількість репозиторіїв

# Дослідити інформацію щодо репозиторіїв
repo_dicts = response_dict['items']  # Значення пов'язане з 'items' - це список,
# що містить низку словників, кожен з яких зберігає данні що до одного окремого сховища Python
# Зберігаємо цей список словників в repo_dicts

print(f"Repositories returned: {len(repo_dicts)}")  # Виводимо загальну кількість репозиторіїв

# Дослідити перший репозиторій
repo_dict = repo_dicts[0]  # Зберігаємо перший словник у repo_dict
print(f"\nKeys: {len(repo_dict)}")  # Виводимо кількість його ключів
for key in sorted(repo_dict.keys()):  # Виводимо всі ключі
    print(key)

