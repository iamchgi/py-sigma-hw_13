"""
Базовий алгоритм швидкого сортування
Time Complexity: O(n^2) worst case, O(n log(n)) - average
Auxiliary Space: O(1)
"""
import numpy

from busy_time_meter import busy_time_meter


# Функція пошуку положення роздільного елементу
def partition(array, low, high):
    # виберіть крайній правий елемент як опорний
    pivot = array[high]

    # покажчик для більшого за low елемента
    i = low - 1

    # пройти через усі елементи  порівняйте кожен елемент із опорним
    for j in range(low, high):
        if array[j] <= pivot:
            # Якщо знайдено елемент, менший за опорний поміняти його місцями на більший елемент, позначений як i
            i = i + 1

            # Заміна елемента i на елемент j
            (array[i], array[j]) = (array[j], array[i])

    # поміняйте опорний елемент на більший, визначений як i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Повернення позиції розділу
    return i + 1


# Функція швидкого сортування
def quick_sort(array, low, high) -> numpy.ndarray:
    if low < high:
        # Знайти такий опорний елемент, що
        #   елемент, менший за опору, розташовано ліворуч
        #   елемент, більший за ось, розташовано праворуч
        pi = partition(array, low, high)

        # Рекурсивний виклик ліворуч від опорного елемента
        quick_sort(array, low, pi - 1)

        # Рекурсивний виклик праворуч від опорного елемента
        quick_sort(array, pi + 1, high)
    return array


@busy_time_meter
def quick_sort_array(array) -> numpy.ndarray:
    return quick_sort(array, 0, len(array) - 1)
