from datetime import time


def log(filename="empty"):
    """
    Декоратор для логирования вызова функции в текстовый файл или консоль.

    :param filename: Название файла для логирования. Если не указано, лог выводится в консоль.
    """

    def wrapper(function):
        def inner(*args, **kwargs):
            try:
                time_start = time()
                result = function(*args, **kwargs)
                time_end = time()
                log_message = f"{function.__name__} ok, начало выполнения функции - {time_start}, конец выполнения функции - {time_end}"
            except Exception as e:
                result = ""
                log_message = f"{function.__name__} error: {str(e)}. Inputs: {args}, {kwargs}"
            if filename != "empty":
                with open(filename, "a") as my_file:
                    my_file.write(log_message + "\n")
            else:
                print(log_message)
            return result

        return inner

    return wrapper


if __name__ == "__main__":

    @log()
    def my_function(x, y):
        return x + y

    my_function(1, "2")
