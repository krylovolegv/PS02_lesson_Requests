import requests
# URL для поиска репозиториев на GitHub
url = 'https://api.github.com/search/repositories'
# Параметры запроса
params = {
    'q': 'language:html',  # Поиск репозиториев с кодом на HTML
    'sort': 'stars',  # Сортировка по количеству звезд
    'order': 'desc'  # Порядок сортировки: убывающий
}
# Отправка GET-запроса
response = requests.get(url, params=params)
# Печать статус-кода ответа
print('Status Code:', response.status_code)
# Печать содержимого ответа в формате JSON
print('Response JSON:')
print(response.json())  # Метод .json() преобразует ответ в формате JSON в словарь Python