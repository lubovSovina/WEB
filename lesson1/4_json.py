import json

with open('files/cats_json.json') as cat_file:
    data = json.load(cat_file)  # считывает целиком файл в формате JSON и возвращает объекты Python
for key, value in data.items():
    if type(value) == list:
        print(f'{key}: {", ".join(value)}')
    else:
        print(f'{key}: {value}')

s = 'Не Json'
json.loads(s)  # считывает строку в формате JSON и возвращает объекты Python

# Чтобы воспользоваться методом loads(), нужно сначала считать весь файл в строку,
# а затем передать ее методу для преобразования в json-объект.
with open('files/cats_2.json') as cat_file:
    f = cat_file.read()
    data = json.loads(f)
    for item in data:
        for key, value in item.items():
            if type(value) == list:
                print(f'{key}: {", ".join(value)}')
            else:
                print(f'{key}: {value}')
        print()

cats_dict = {
    'name': 'Pushin',
    'age': 1,
    'meals': [
        'Purina', 'Cat Chow', 'Hills'
    ],
    'owners': [
        {
            'first_name': 'Bill',
            'last_name': 'Gates'
        },
        {
            'first_name': 'Melinda',
            'last_name': 'Gates'
        }
    ]
}
with open('files/cats_3.json', 'w') as cat_file:
    json.dump(cats_dict, cat_file)  # метод записывает объект Python в файл в формате JSON

weekdays = {i: day
            for i, day in enumerate(['Sunday',
                                     'Monday',
                                     'Tuesday',
                                     'Wednesday',
                                     'Thursday',
                                     'Friday',
                                     'Saturday'
                                     ])}
data = json.dumps(weekdays)  # метод преобразует объект Python в строку в формате JSON
print(data)

# если ensure_ascii=True (по умолчанию), все не-ASCII символы в выводе будут
# экранированы последовательностями \uXXXX. Если ensure_ascii=False, эти символы будут записаны как есть.
# Это важно, если в содержимом есть русские буквы.

with open('files/cats_4.json', 'w') as file:
    json.dump(data, file, ensure_ascii=False)

# Отступ indent нужен для удобного для чтения человеком представления информации в объекте JSON.
# По умолчанию имеет значение None для более компактного представления, то есть без отступов.
with open('files/cats_5.json', 'w') as file:
    json.dump(data, file, ensure_ascii=False, indent=2)

# Если sort_keys=True (по умолчанию False), ключи выводимого словаря будут отсортированы.
# Это удобно, если ключей много.
with open('files/cats_6.json', 'w') as file:
    json.dump(data, file, ensure_ascii=False,
              indent=2, sort_keys=True)

