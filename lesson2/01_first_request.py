# программа, выполняющая запрос к серверу, анализирующая код ответа и в случае успешного запроса печатающая полученную
# страницу, выглядит следующим образом
import requests

# Готовим запрос.
geocoder_request = "http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&" \
                   "geocode=Якутск&format=json"

# Выполняем запрос.
response = requests.get(geocoder_request)
if response:
    # Запрос успешно выполнен, печатаем полученные данные.
    print(response.content)
else:
    # Произошла ошибка выполнения запроса. Обрабатываем http-статус.
    print("Ошибка выполнения запроса:")
    print(geocoder_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
