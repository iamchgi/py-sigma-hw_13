"""
Виконав: Григорій Чернолуцький
Homework_12

"""
import os
import random
import sys
import time

import numpy as np
from matplotlib import pyplot as plt
from sorting_engines import sort_sort, np_sort_stable, np_sort_heapsort, np_sort_quicksort, \
    np_sort_mergesort, bubble_sort, quick_sort_array, merge_sort_array, insertion_sort, coolest_sort, tim_sort
from dao import save_bin_file, read_bin_file


def show_result_image(S, text) -> None:
    """
    Функція візуалізації дискретного ряду
    :param S: вхідний масив дискретних даних
    :param text: повідомлення
    :return: нічого
    """
    plt.plot(S)
    plt.ylabel(text)
    plt.show()
    return None


# ----------------------- рівномірний закон розводілу - десяткове числення -----------------------
def random_uniform(a, b, iter) -> np.array:
    """
    Функція генерування випадкових величин за рівномірним законом - float
    :param a: ліва межа зміни значень / довірчого інтервала
    :param b: права межа зміни значень / довірчого інтервала
    :param iter: кількість елементів, що генерується
    :return: вибірка значень рівномірно розподілених в межах a, b, з кількістю iter - десяткова система числення
    """
    S = np.zeros((iter))
    for i in range(iter):
        S[i] = np.random.uniform(a, b)  # параметри закону задаються межами аргументу
    return S


# ----------------------- рівномірний закон розподілу - цілі числа -----------------------
def random_uniform_int(a, b, iter) -> np.array:
    """
    Функція генерування випадкових величин за рівномірним законом з параметрами - int
    :param a: ліва межа зміни значень / довірчого інтервала
    :param b: права межа зміни значень / довірчого інтервала
    :param iter: кількість елементів, що генерується
    :return: вибірка значень рівномірно розподілених в межах a, b, з кількістю iter - десяткова система числення
    """
    S = np.zeros(iter, dtype=int)
    for i in range(iter):
        S[i] = random.randint(a, b)  # параметри закону задаються межами аргументу
    return S


def init_test(a, b, iter, type) -> np.array:
    """
    Метод реалізує приготування для тестування алгоритмів сортування
    :param a: Початок діапазону випадкових чисел
    :param b: Кінець діапазону випадкових чисел
    :param iter: Кількість випадкових чисел
    :param type: Тип випадкових чисел
    :return: Сгенерований масив випадкових чисел
    """
    filename_start = 'data_sets/unsorted_' + str(a) + "_" + str(b) + "_" + str(iter) + "_" + type + '.pkl'
    if os.path.exists(filename_start):
        random_arr = read_bin_file(filename_start)
    else:
        start_time = time.time()
        if type == 'int':
            # ---------------------- сортування випадкового масиву int ---------------------------
            random_arr = random_uniform_int(a, b, iter)
        else:
            # ---------------------- сортування випадкового масиву float ---------------------------
            random_arr = random_uniform(a, b, iter)
        end_time = time.time()
        # Різниця часу
        execution_time = end_time - start_time
        print(f"Час генерації набору випадкових чисел: {execution_time:.6f} секунд")

        save_bin_file(random_arr, filename_start)  # запис випадкового масиву у файл
    show_result_image(random_arr, 'random.uniform')  # графік візуалізації вхідних не сортованих даних
    return random_arr


def finalize_test(arr, a, b, iter, type) -> None:
    """
    Метод - завершення тестування. Візуалізація і збереження результату.
    :param arr: Відсортований масив
    :param a: Початок діапазону випадкових чисел
    :param b: Кінець діапазону випадкових чисел
    :param iter: Кількість випадкових чисел
    :param type: Тип випадкових чисел
    :return: нічого
    """
    filename_stop = 'data_sets/sorted_' + str(a) + "_" + str(b) + "_" + str(iter) + "_" + type + '.pkl'
    show_result_image(arr, 'random.uniform.sort')  # графік візуалізації сортованих даних
    save_bin_file(arr, filename_stop)  # запис сортованого масиву у файл
    return None


# --------------------------------- main module ----------------------------------------------
if __name__ == '__main__':
    # ---------------------- вихідні параметри об'єкта сортування ----------------------------
    begin = 0
    end = 1_000
    iter = 10_000
    type = 'int'
    unsorted_arr = init_test(begin, end, iter, type)
    sys.setrecursionlimit(10000)
    sorted_arr = bubble_sort(unsorted_arr.copy())  # сортування бульбашкою 55s 0-100 10000 int
    sorted_arr = insertion_sort(unsorted_arr.copy())  # 25s 0-1000 10000 int
    sorted_arr = quick_sort_array(unsorted_arr.copy())
    sorted_arr = merge_sort_array(unsorted_arr.copy())
    sorted_arr = np_sort_quicksort(unsorted_arr.copy())
    sorted_arr = np_sort_mergesort(unsorted_arr.copy())
    sorted_arr = np_sort_heapsort(unsorted_arr.copy())
    sorted_arr = np_sort_stable(unsorted_arr.copy())
    sorted_arr = coolest_sort(unsorted_arr.copy())  # Timsort вбудоване  (create new array)
    sorted_arr = sort_sort(unsorted_arr.copy())  # алгоритм Timsort вбудоване (use old array)
    sorted_arr = tim_sort(unsorted_arr.copy())  # Timsort
    finalize_test(sorted_arr, begin, end, iter, type)

"""
РЕЗУЛЬТАТ

Файл compare_all.txt - збір всіх результатів тестування в скороченому варіанті
Файл compare_full.txt - приклад детального варіанту розбору результату

"""
