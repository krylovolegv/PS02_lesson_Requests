import requests
# URL для создания нового поста
url = 'https://jsonplaceholder.typicode.com/posts'
# Словарь с данными, который мы хотим отправить
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}
# Отправка POST-запроса
response = requests.post(url, json=data)
# Вывод статус-кода ответа
print('Status Code:', response.status_code)
# Вывод содержимого ответа
print('Response Content:', response.json())