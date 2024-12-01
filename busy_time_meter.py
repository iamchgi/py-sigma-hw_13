"""
Декоратор, додає вимірювання часу витрачене на роботу методу

"""
import cProfile
import time


def busy_time_meter(func):
    def wrapper(*args, **kwargs):
        # Початок виміру
        start_time = time.time()
        # Використання сервісів -------------------
        # cp = cProfile.Profile()  # аналітика складності
        # cp.enable()
        result = func(*args, **kwargs)
        # Кінець виміру
        # cp.disable()
        # cp.print_stats()
        end_time = time.time()
        # Різниця часу
        execution_time = end_time - start_time
        func_name = func.__name__
        print(f"Функція - {func_name:20} час виконання: {execution_time:.6f} секунд")
        return result
    return wrapper