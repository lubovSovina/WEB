import os

print(dir(os))  # всё что находится внутри os

print(os.name)
# posix — для linux и macOS
# nt — для операционных систем семейства Windows
# java — для систем, работающих в виртуальной Java-машине (например, Android)

print(os.getcwd())  # имя текущего каталога


os.chdir('files')  # смены текущего каталога
print(os.getcwd())

os.chdir('..')  # из текущего каталога в родительский
print(os.getcwd())


# существует ли файл, доступен ли файл для чтения или записи
print(os.access("1.txt", os.F_OK))
print(os.access("1.txt", os.R_OK))
print(os.access("1.txt", os.W_OK))


print(os.listdir())  # получение списка файлов и вложенных каталогов
# можно передать относительный или абсолютный адрес каталога

# функция рекурсивного прохода по всем папкам в заданной папке
for currentdir, dirs, files in os.walk('files'):
    print(currentdir, dirs, files)

print(dir(os.path))  # какие функции нам предлагает модуль os.path

os.path.exists('files/3')  # проверить, существует ли файл

os.path.isfile('files/3')  # файл ли
os.path.isdir('files/2')  # папка ли

os.path.abspath('1.txt')  # вернет абсолютный путь по относительному