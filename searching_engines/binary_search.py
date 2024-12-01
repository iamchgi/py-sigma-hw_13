
"""
Алгоритм бінарного (дихотомічного) пошуку - binary (bisection) search
Time Complexity: O(log n)
Auxiliary Space: O(logn)     [NOTE: Recursion creates Call Stack]
Auxiliary Space: O(1)        [NOTE: For Iterative]
Особливості:
застосовується для відсортованих даних;
проблемний для виявлення повторюваних елементів.

"""
from busy_time_meter import busy_time_meter


def binary_search_recursive(arr, low, high, x):
    """
    Класична реалізація алгоритму бінарного пошуку з РЕКУРСИВНИМ викликом
    :param arr: масив даних
    :param low: ліва частинка інтервалу пошуку елемента
    :param high: права частинка інтервалу пошуку елемента
    :param x: ключ пошуку
    :return: позиція ключа
    """
    # Перевірка базового випадку - знайдений елемент на середині масиву
    if high >= low:
        mid = (high + low) // 2
        # Якщо елемент присутній у самій середині
        if arr[mid] == x:
            return mid
        # Якщо елемент менший за середину, то він може бути присутнім лише у лівому підмасиві
        elif arr[mid] > x:
            return binary_search_recursive(arr, low, mid - 1, x)
        # Інакше елемент може бути присутнім лише у правому підмасиві
        else:
            return binary_search_recursive(arr, mid + 1, high, x)
    else:
        # Елемент відсутній у масиві
        return -1

@busy_time_meter
def binary_search_r(arr, x):
    return binary_search_recursive(arr,  0, len(arr) - 1, x)


def binary_search_many_elements(arr, low, high, x):
    """
    Класична реалізація алгоритму бінарного пошуку з РЕКУРСИВНИМ викликом
    особливість - спроба накопичення ключів у списку
    """
    arr_key_position = []
    # Перевірка базового випадку - знайдений елемент на середині масиву
    if high >= low:
        mid = (high + low) // 2
        # Якщо елемент присутній у самій середині
        if arr[mid] == x:
            return mid
        # Якщо елемент менший за середину, то він може бути присутнім лише у лівому підмасиві
        elif arr[mid] > x:
            key_position = binary_search_many_elements(arr, low, mid - 1, x)
            arr_key_position.append(key_position)
            return arr_key_position
        # Інакше елемент може бути присутнім лише у правому підмасиві
        else:
            key_position = binary_search_many_elements(arr, mid + 1, high, x)
            arr_key_position.append(key_position)
            return arr_key_position
    else:
        # Елемент відсутній у масиві
        return arr_key_position.append(-1)

@busy_time_meter
def binary_search_many(arr,x):
    return binary_search_many_elements(arr, 0, len(arr) - 1, x)

@busy_time_meter
def binary_search_iterative(arr, x):
    """
    Класична реалізація алгоритму бінарного пошуку з РЕКУРЕНТНИМ викликом
    особливість - спроба накопичення ключів у списку
    """
    low = 0
    high = len(arr) - 1
    # mid = 0
    while low <= high:
        mid = (high + low) // 2
        # кщо x більше, ліву половину ігнорувати
        if arr[mid] < x:
            low = mid + 1
        # Якщо x менше, ігноруйте праву половину
        elif arr[mid] > x:
            high = mid - 1
        # x присутній у середині
        else:
            return mid
    # Елемент відсутній у масиві
    return -1