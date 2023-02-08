# можно передавать параметры в ту функцию, которую мы хотим вызывать
import schedule

i = 0


def greet(name):
    global i
    print('Hello', name)
    i += 1
    if i == 5:
        return schedule.CancelJob # Отменяем задачу после 5 запуска


schedule.every(1).to(3).seconds.do(greet, name='Yandex')
# Запускаем задачу в случайное время время от 1 до 3 секунд

while True:
    schedule.run_pending()