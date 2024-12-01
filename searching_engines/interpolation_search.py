
"""
Алгоритм інтерполяційного пошуку - interpolation search
Суть - в пошуку роздільного елементу - прогнозування / екстраполяція - за законом розподілу значень у вибірці

Time Complexity: O(log n) для середнього випадку та O(n) для найгіршого випадку
Auxiliary Space Complexity: O(1)

Особливості:
застосовується для відсортованих даних;
проблемний для виявлення повторюваних елементів.

"""
from busy_time_meter import busy_time_meter


def interpolation_search_recursive(arr, lo, hi, x):
    """
    Інтерполяційний пошук з РЕКУРСІЄЮ
    :param arr: вхфдний масив
    :param lo: початок інтервалу пошуку ключа
    :param hi: кінець інтервалу пошуку ключа
    :param x: ключ пошуку
    :return: позиція ключа
    """

    # Оскільки масив відсортовано, шуканий елемент має бути присутній у масиві в діапазоні:
    if (lo <= hi and x >= arr[lo] and x <= arr[hi]):
        # Пошук положення ключа з передбаченням лінійного розподілу значень утриманням
        pos = int(lo + ((hi - lo) // (arr[hi] - arr[lo]) * (x - arr[lo])))      #  УВАГА: виправлено помилку - явна трансформація до цілих чисел.
        # Ключ знайдено
        if arr[pos] == x:
            return pos
        # Якщо x більше - то ключ знаходиться в правому підмасиві
        if arr[pos] < x:
            return interpolation_search_recursive(arr, pos + 1, hi, x)
        # Якщо x менше то ключ знаходиться в лівому підмасиві
        if arr[pos] > x:
            return interpolation_search_recursive(arr, lo, pos - 1, x)
    return -1

@busy_time_meter
def interpolation_search_r(arr,x):
    return interpolation_search_recursive(arr, 0, (len(arr) - 1), x)

@busy_time_meter
def interpolation_search_iterative(arr, x):
    """
    Інтерполяційний пошук з РЕКУРЕНТНІСТЮ
    :param arr: вхідний масив
    :param x: ключ пошуку
    :return: позиція ключа
    """

    # Визначення параметрів діапазону пошуку ключа
    low = 0
    n = len(arr)
    high = (n - 1)
    # Оскільки масив відсортовано, шуканий елемент має бути присутній у масиві в діапазоні:
    while low <= high and x >= arr[low] and x <= arr[high]:
        if low == high:
            if arr[low] == x:
                return low
            return -1
        # Пошук положення ключа з передбаченням лінійного розподілу значень утриманням
        pos = int(low + (((float(high - low) / (arr[high] - arr[low])) * (x - arr[low]))))
        # Ключ знайдено
        if arr[pos] == x:
            return pos
        # Якщо х більше то ключ знаходиться у верхній частині масиву
        if arr[pos] < x:
            low = pos + 1
        # Якщо х менше то ключ знаходиться у нижній частині масиву
        else:
            high = pos - 1
    return -1
