"""

Особливості Timsort:
Складність:
Найпоганіший випадок:
𝑂(𝑛log⁡𝑛)
O(nlog n)
Кращий випадок:
𝑂(𝑛)
O(n) (якщо масив вже відсортовано або майже відсортовано)
Середній випадок:
𝑂(𝑛log⁡𝑛)O(nlog n)
Стабільність:
Timsort є стабільним алгоритмом (не змінює порядок рівних елементів).
Ефективність:
Добре працює на реальних даних, які часто мають частково відсортовані фрагменти.

"""
from busy_time_meter import busy_time_meter


def insertion_sort(arr, left, right):
    """Сортировка вставками на диапазоне от left до right."""
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge(arr, temp, left, mid, right):
    """Слияние двух отсортированных частей массива."""
    i, j, k = left, mid + 1, left

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:  # Оставшиеся элементы из левой части
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:  # Оставшиеся элементы из правой части
        temp[k] = arr[j]
        j += 1
        k += 1

    # Копируем обратно в исходный массив
    for i in range(left, right + 1):
        arr[i] = temp[i]


@busy_time_meter
def tim_sort(arr):
    """Главная функция Timsort."""
    n = len(arr)
    MIN_RUN = 32

    # Шаг 1: Разбить массив на пробеги и отсортировать их вставками
    for start in range(0, n, MIN_RUN):
        end = min(start + MIN_RUN - 1, n - 1)
        insertion_sort(arr, start, end)

    # Шаг 2: Слияние пробегов с удвоением размера
    size = MIN_RUN
    temp = [0] * n  # Временный массив для слияния
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)

            if mid < right:
                merge(arr, temp, left, mid, right)

        size *= 2

    return arr
