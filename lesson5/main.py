import requests

geocoder_request = "http://static-maps.yandex.ru/1.x/?ll=37.530887,55.703118&spn=0.002,0.002&l=map"

response = requests.get(geocoder_request)
if response:
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
else:
    print('Ошибка выполнения запроса:')
    print(geocoder_request)
    print('Http status:', response.status_code, '(', response.reason, ')')
