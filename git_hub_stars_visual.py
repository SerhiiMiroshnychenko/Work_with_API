import requests

from plotly.graph_objs import Bar
from plotly import offline

# Зробити виклик через API та зберегти відповідь
url = 'https://api.github.com/search/repositories?q=repositories&sort=stars'  # Зберігаємо URL
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
names, stars, languages, colors = [], [], [], []
colors_dict = {
    "C++": 'gray',
    "C": 'gray',
    "Python": 'blue',
    "JavaScript": 'yellow',
    "TypeSkript": 'orange',
    "Vim Script": 'orange',
    "Shell": 'white',
    "": 'rgb(60, 100, 150)',
    "PowerShell": 'white',
    "PHP": 'purple',
    "Go": 'rgb(100, 150, 200)',
    "Jupiter Notebook": 'rgb(50, 50, 200)',
}
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_language = repo_dict['language']
    if repo_language in colors_dict:
        color = colors_dict[repo_language]
    else:
        color = 'rgb(25, 25, 25)'
    stars.append(repo_dict['stargazers_count'])
    languages.append(repo_language)  # Мова
    names.append(repo_name)
    colors.append(color)


# Зробити візуалізацію
data = [{
    'type': 'bar',  # Тип діаграми: стовпчикова
    'x': names,  # Вісь х: посилання
    'y': stars,  # Вісь у: зірочки
    'hovertext': languages,  # Підказки
    'marker': {
        'color': colors,  # Блакитний колір стовпчиків
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
offline.plot(fig, filename='git_hub_stars.html')

