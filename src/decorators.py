

def log(logs, error_message, filename='empty'):
    def wrapper(function):
        def inner():
            print('начало')
            if filename != 'empty':
                my_file = open(str(filename), "w+")
                my_file.write(logs)
                my_file.close()
            else:
                print(logs)
            print('конец')
            return function()
        return inner
    return wrapper

if __name__ == "__main__":
    @log(error_message='ошибка', logs='надпись', filename='file_logs.txt')
    def my_function():
        return ''
    print(my_function())