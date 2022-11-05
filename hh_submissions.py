from operator import itemgetter

import requests

# Зробити виклик через API та зберегти відповідь
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f'Status code: {r.status_code}')  # Виводимо на екран статус виклику

# Обробити інформацію щодо кожної публікації
submission_ids = r.json()  # Конвертуємо об'єкт відповіді в список Python
submission_dicts = []  # Започатковуємо порожній список для зберігання словників

for submission_id in submission_ids[:30]:  # Проходимо циклом по ID 30 найпопулярніших статей
    # Зробити окремий виклик через API для кожного допису
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"  # Для кожної публікації
    # генеруємо url виклику
    r = requests.get(url)  # Робимо виклик через API
    print(f"id: {submission_id}\tstatus: {r.status_code}")  # Виводимо статус виклику
    response_dict = r.json()  # Зберігаємо результат відповіді на API виклик у змінну

    # Зробити словник для кожного допису
    submission_dict = {
        'title': response_dict['title'],  # Назва допису
        'hh_link': f"http://news.ycombinator.com/item?id={submission_id}",  # Посилання
        'comments': response_dict['descendants'],  # Кількість коментарів
    }
    submission_dicts.append(submission_dict)  # Додаємо кожен сформований словник до списку

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)  # Видобуваємо за допомогою
# функції itemgetter значення пов'язані з ключем 'comments' та сортуємо список за цими значеннями

for submission_dict in submission_dicts:  # Проходим циклом по списку
    print(f"\nTitle: {submission_dict['title']}")  # Виводимо назву
    print(f"Discussion link: {submission_dict['hh_link']}")  # Посилання
    print(f"Comments: {submission_dict['comments']}")  # Та кількість коментарів
