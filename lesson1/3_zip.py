from zipfile import ZipFile

# выведет на экран содержание архива, который мы создали ранее, используя арсенал библиотеки shutil
with ZipFile('archive.zip') as myzip:
    myzip.printdir()

# получать информацию о файлах в архиве в виде списка
with ZipFile('archive.zip') as myzip:
    info = myzip.infolist()

# имена файлов в архиве, тоже в виде списка
with ZipFile('archive.zip') as myzip:
    print(myzip.namelist())

# «вытащим» из архива конкретный файл
with ZipFile('archive.zip') as myzip:
    with myzip.open('1.txt', 'r') as file:
        print(file.read())

# мы знаем, что перед нами — текстовый файл, поэтому мы можем быстро преобразовать (декодировать)
# эту строку. Надо только помнить, в какой кодировке записан файл.
with ZipFile('archive.zip') as myzip:
    with myzip.open('1.txt', 'r') as file:
        print(file.read().decode('utf-8'))

# по аналогии с чтением файлов из архива их можно туда и записывать
with ZipFile('archive.zip', 'w') as myzip:
    myzip.write('test.txt')
    print(myzip.namelist())

# для добавления файла в уже существующий архив будем работать с ним с ключом a
with ZipFile('archive.zip', 'a') as myzip:
    myzip.write('test.txt')
    print(myzip.namelist())

# вытаскивает из архива все содержимое в указанную папку
ZipFile.extractall(path=None, members=None, pwd=None)
