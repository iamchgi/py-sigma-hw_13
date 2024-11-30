"""
Найкрутіше сортування
Time Complexity: ?
Auxiliary Space: ?

Що таке функція sort() Python?
https://www.geeksforgeeks.org/sort-in-python/
У Python sort()функція — це метод, який належить до списку.
Він використовується для сортування в python або елементів списку в порядку зростання за замовчуванням.
Метод sort()змінює оригінальний список на місці, тобто він змінює порядок елементів безпосередньо в існуючому об’єкті списку,
а не створює новий відсортований список.

"quicksort" (по умолчанию)
"mergesort"
"heapsort"
"stable" (начиная с NumPy 1.15).
numpy.sort(a, axis=-1, kind=None, order=None)

kind : {'quicksort', 'mergesort', 'heapsort', 'stable'}, optional
        Sorting algorithm. The default is 'quicksort'. Note that both 'stable'
        and 'mergesort' use timsort or radix sort under the covers and,
        in general, the actual implementation will vary with data type.
        The 'mergesort' option is retained for backwards compatibility.

"""

import numpy as np
from busy_time_meter import busy_time_meter

# сортування методами numpy
@busy_time_meter
def np_sort_quicksort(arr):
    return np.sort(arr, kind="quicksort")

@busy_time_meter
def np_sort_mergesort(arr):
    return np.sort(arr,kind="mergesort")

@busy_time_meter
def np_sort_heapsort(arr):
    return np.sort(arr,kind="heapsort")

@busy_time_meter
def np_sort_stable(arr):
    return np.sort(arr,kind="stable")

# сортування  Timsort
@busy_time_meter
def coolest_sort(arr):
    coolest_sorted = sorted(arr)
    return (coolest_sorted)

# алгоритм Timsort
@busy_time_meter
def sort_sort(arr):
    arr.sort()
    return arr


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
