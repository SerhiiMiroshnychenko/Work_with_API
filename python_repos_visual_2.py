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
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a"  # Формуємо посилання
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']  # Власник
    description = repo_dict['description']  # Опис
    label = f"{owner}<br />{description}"  # Формуємо інформацію
    labels.append(label)

# Зробити візуалізацію
data = [{
    'type': 'bar',  # Тип діаграми: стовпчикова
    'x': repo_links,  # Вісь х: посилання
    'y': stars,  # Вісь у: зірочки
    'hovertext': labels,  # Підказки
    'marker': {
        'color': 'rgb(60, 100, 150)',  # Блакитний колір стовпчиків
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}  # Сірий колір завтовшки 1,5 пікселей
    },
    'opacity': 0.6,  # Прозорість стовпчиків 0,6
}]

my_layout = {  # Опис компонування, назви діаграми та осей
    'title': 'Найбільш зіркові Python проєкти на GitHub',
    'titlefont': {'size': 28},  # Розмір шрифту в назві діаграми
    'xaxis': {
        'title': 'Репозиторії',
        'titlefont': {'size': 24},  # Розмір літер в назві осі х
        'tickfont': {'size': 14},  # Розмір літер підписів для розмітки
    },
    'yaxis': {
        'title': 'Зірки',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')

