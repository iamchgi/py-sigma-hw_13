"""
Виконав: Григорій Чернолуцький
Homework_13

Package                      Version
---------------------------- -----------
pip                          24.3.1
numpy                        2.1.3
matplotlib                   3.9.2

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
from searching_engines import np_search, linear_search_one_element, linear_search_many_elements, \
    interpolation_search_r, interpolation_search_iterative, binary_search_iterative, \
    binary_search_many, binary_search_r, insert_node, search_node_recursion, BinThree


def show_result_image(s, text) -> None:
    """
    Функція візуалізації дискретного ряду
    :param s: вхідний масив дискретних даних
    :param text: повідомлення
    :return: нічого
    """
    plt.plot(s)
    plt.ylabel(text)
    plt.show()
    return None


# ----------------------- рівномірний закон розводілу - десяткове числення -----------------------
def random_uniform(a, b, n) -> np.array:
    """
    Функція генерування випадкових величин за рівномірним законом - float
    :param a: ліва межа зміни значень / довірчого інтервала
    :param b: права межа зміни значень / довірчого інтервала
    :param n: кількість елементів, що генерується
    :return: вибірка значень рівномірно розподілених в межах a, b, з кількістю iter - десяткова система числення
    """
    s = np.zeros(n)
    for i in range(n):
        s[i] = np.random.uniform(a, b)  # параметри закону задаються межами аргументу
    return s


# ----------------------- рівномірний закон розподілу - цілі числа -----------------------
def random_uniform_int(a, b, n) -> np.array:
    """
    Функція генерування випадкових величин за рівномірним законом з параметрами - int
    :param a: ліва межа зміни значень / довірчого інтервала
    :param b: права межа зміни значень / довірчого інтервала
    :param n: кількість елементів, що генерується
    :return: вибірка значень рівномірно розподілених в межах a, b, з кількістю iter - десяткова система числення
    """
    s = np.zeros(n, dtype=int)
    for i in range(n):
        s[i] = random.randint(a, b)  # параметри закону задаються межами аргументу
    return s


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
        # Різниця часу
        execution_time = time.time() - start_time
        print(f"Час генерації набору випадкових чисел: {execution_time:.6f} секунд")

        save_bin_file(random_arr, filename_start)  # запис випадкового масиву у файл
    show_result_image(random_arr, 'random.uniform')  # графік візуалізації вхідних не сортованих даних
    return random_arr


def sort_array(unsorted_arr, a, b, iter, type) -> np.array:
    """
    Метод видає в результаті відсортований масив
    :param unsorted_arr: Невідсортований масив
    :param a: Початок діапазону випадкових чисел
    :param b: Кінець діапазону випадкових чисел
    :param iter: Кількість випадкових чисел
    :param type: Тип випадкових чисел
    :return: Відсортований(здобутий де інде) масив випадкових чисел
    """
    sorted_arr_filename = 'data_sets/sorted_' + str(a) + "_" + str(b) + "_" + str(iter) + "_" + type + '.pkl'
    if os.path.exists(sorted_arr_filename):
        sorted_arr = read_bin_file(sorted_arr_filename)
    else:
        # sys.setrecursionlimit(10000)
        # sorted_arr = bubble_sort(unsorted_arr.copy())  # сортування бульбашкою 55s 0-100 10000 int
        # sorted_arr = insertion_sort(unsorted_arr.copy())  # 25s 0-1000 10000 int
        # sorted_arr = quick_sort_array(unsorted_arr.copy())
        # sorted_arr = np.array(merge_sort_array(unsorted_arr.copy()))
        # sorted_arr = np_sort_quicksort(unsorted_arr.copy())
        # sorted_arr = np_sort_mergesort(unsorted_arr.copy())
        # sorted_arr = np_sort_heapsort(unsorted_arr.copy())
        # sorted_arr = np_sort_stable(unsorted_arr.copy())
        # sorted_arr = np.array(coolest_sort(unsorted_arr.copy()))  # Timsort вбудоване  (create new array)
        sorted_arr = sort_sort(unsorted_arr.copy())  # алгоритм Timsort вбудоване (use old array)
        # sorted_arr = tim_sort(unsorted_arr.copy())  # Timsort
    return sorted_arr


def looking_for(sorted_arr, key) -> None:
    """
    Метод щось шукає
    :param sorted_arr: Відсоортований масив
    :param key: Елемент який будемо шукати
    :return:
    """
    sys.setrecursionlimit(10000)
    print(f"key = {key}")
    print(np_search(key, sorted_arr))
    print(linear_search_one_element(key, sorted_arr))
    print(linear_search_many_elements(key, sorted_arr))
    print(interpolation_search_r(sorted_arr, key))  # екстраполяційний пошук
    print(interpolation_search_iterative(sorted_arr, key))
    print(binary_search_r(sorted_arr, key))  # бінарний пошук
    print(binary_search_many(sorted_arr, key))
    print(binary_search_iterative(sorted_arr, key))
    start_time = time.time()
    root = None
    root = insert_node(root, unsorted_arr[0])
    for i in range(1, iter):
        insert_node(root, unsorted_arr[i])
    # Різниця часу
    execution_time = time.time() - start_time
    print(f"Час створення recursion three: {execution_time:.6f} секунд")
    found = search_node_recursion(root, key)
    if found is None:
        print(key, "not found")
    else:
        print(found.key, "found")
    start_time = time.time()
    three = BinThree()
    for i in range(iter):
        three.insert(unsorted_arr[i])
    # Різниця часу
    execution_time = time.time() - start_time
    print(f"Час створення class three: {execution_time:.6f} секунд")
    found = three.search(key)
    if found is None:
        print(key, "not found")
    else:
        print(found.key, "found")
    return None


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
    sorted_arr_filename = 'data_sets/sorted_' + str(a) + "_" + str(b) + "_" + str(iter) + "_" + type + '.pkl'
    show_result_image(arr, 'random.uniform.sort')  # графік візуалізації сортованих даних
    if os.path.exists(sorted_arr_filename):
        save_bin_file(arr, sorted_arr_filename)  # запис сортованого масиву у файл
    return None


# --------------------------------- main module ----------------------------------------------
if __name__ == '__main__':
    # ---------------------- вихідні параметри об'єкта сортування ----------------------------
    begin = 0
    end = 10_000
    iter = 10_000
    type = 'int'
    unsorted_arr = init_test(begin, end, iter, type)
    sorted_arr = sort_array(unsorted_arr, begin, end, iter, type)
    key = unsorted_arr[random.randint(0, iter)]
    looking_for(sorted_arr, key)
    finalize_test(sorted_arr, begin, end, iter, type)

"""
РЕЗУЛЬТАТ

# Файл compare_all.txt - збір всіх результатів тестування в скороченому варіанті
# Файл compare_full.txt - приклад детального варіанту розбору результату

"""
