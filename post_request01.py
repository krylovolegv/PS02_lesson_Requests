import requests
url = 'https://jsonplaceholder.typicode.com/posts' # URL для получения постов
# Параметры запроса
params = {
    'userId': 1  # Получаем посты пользователя с userId = 1
}
response = requests.get(url, params=params) # Отправка GET-запроса
# Проверка статуса ответа
if response.status_code == 200:
    # Вывод полученных записей
    posts = response.json()  # Преобразование ответа из JSON в список словарей Python
    for post in posts:
        print(post)
else:
    print(f"Не удалось получить сообщения. Код состояния: {response.status_code}")