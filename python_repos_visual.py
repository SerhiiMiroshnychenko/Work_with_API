import requests

from plotly.graph_objs import Bar
from plotly import offline

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
repo_dicts = response_dict['items']  # Значення пов'язане з 'items' - це список,
# що містить низку словників, кожен з яких зберігає данні що до одного окремого сховища Python
# Зберігаємо цей список словників в repo_dicts
repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Зробити візуалізацію
data = [{
    'type': 'bar',  # Тип діаграми: стовпчикова
    'x': repo_names,  # Вісь х: назви репозиторіїв
    'y': stars,  # Вісь у: зірочки
    'marker': {
        'color': 'rgb(60, 100, 150)',  # Блакитний колір стовпчиків
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}  # Сірий колір завтовшки 1,5 пікселей
    },
    'opacity': 0.6,  # Прозорість стовпчиків 0,6
}]

my_layout = {  # Опис компонування, назви діаграми та осей
    'title': 'Найбільш зіркові Python проєкти на GitHub',
    'xaxis': {'title': 'Репозиторії'},
    'yaxis': {'title': 'Зірки'},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')

