def some_func():
    print('func is running')
    if __name__ == '__main__':
        print('I was called without ##import##')


def main():
    print('Main part of main4.py')
    some_func()

if __name__ == '__main__':
    main()