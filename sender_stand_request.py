import configuration

import requests

import data

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)
response = get_docs()

print(response.status_code)

def get_logs() :
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH)
response = get_logs()
print(response.status_code)
print(response.headers)

def get_logs() :
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,
                        params={"count":20})
response = get_logs()
print(response.status_code)
print(response.headers)

def get_users_table() :
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)
response = get_users_table()
print(response.status_code)

def post_new_user(body):
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
    return response

# Вызов функции post_new_user с телом запроса для создания нового пользователя из модуля data
response = post_new_user(data.user_body)

# Вывод HTTP-статус кода ответа на запрос
# Код состояния указывает на результат обработки запроса сервером
print(response.status_code)