import json

from plotly import offline

p_languages = ['Python', 'Java', 'JavaScript', 'C++', 'PHP', 'Go', 'Swift',
               'C#', 'TypeScript', 'Kotlin', 'Ruby', 'Scala', 'Dart']

colors_dict = {
    'Python': 'rgb(60, 200, 200)',
    'Java': 'orange',
    'JavaScript': 'yellow',
    'C++': 'rgb(60, 100, 150)',
    'PHP': 'purple',
    'Go': 'blue',
    'Swift': 'pink',
    'C#': 'rgb(60, 100, 150)',
    'TypeScript': 'violet',
    'Kotlin': 'brown',
    'Ruby': 'red',
    'Scala': 'green',
    'Dart': 'grey',
}

dict_languages = {}

for p_language in p_languages:
    print(p_language)
    file_name = f'{p_language}.json'
    with open(file_name) as f:
        response_dict = json.load(f)
        total_count = response_dict['total_count']
        print(total_count)
        dict_languages[total_count] = p_language

print(dict_languages)

list_counts = list(dict_languages.keys())
list_counts.sort(reverse=True)

prog_languages, total_counts, colors, info = [], [], [], []

for number in list_counts:
    prog_languages.append(dict_languages[number])
    total_counts.append(round(number, 3))
    colors.append(colors_dict[dict_languages[number]])
    t_c_text = f"{round(number, 3)} млн"
    info.append(f'{dict_languages[number]}:{t_c_text}')


# Зробити візуалізацію
data = [{
    'type': 'bar',  # Тип діаграми: стовпчикова
    'x': prog_languages,  # Вісь х: посилання
    'y': total_counts,  # Вісь у: зірочки
    'hovertext': info,  # Підказки
    'marker': {
        'color': colors,  # Блакитний колір стовпчиків
        'line': {'width': 0.25, 'color': 'rgb(25, 25, 25)'}  # Сірий колір завтовшки 1,5 пікселей
    },
    'opacity': 0.6,  # Прозорість стовпчиків 0,6
}]

my_layout = {  # Опис компонування, назви діаграми та осей
    'title': 'Кількість проєктів на GitHub по мовах програмування',
    'titlefont': {'size': 28},  # Розмір шрифту в назві діаграми
    'xaxis': {
        'title': 'Репозиторії',
        'titlefont': {'size': 24},  # Розмір літер в назві осі х
        'tickfont': {'size': 14},  # Розмір літер підписів для розмітки
    },
    'yaxis': {
        'title': 'Кількість, млн',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='git_hub_languages.html')
