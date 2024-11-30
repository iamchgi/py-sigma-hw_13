"""
Алгоритм сортування вставкою
Time Complexity: O(n^2)
Auxiliary Space: O(1)
"""
from busy_time_meter import busy_time_meter


@busy_time_meter
# Функція алгоритму сортування вставкою
def insertion_sort(arr):
    # Перехід черех 1 до len(arr)
    # Підрахунок ітерацій: метод enumerate() додає лічильник до ітерованого arr і повертає його у формі об’єкта перерахування.
    for i, key in enumerate(arr):

        # Перемістити елементи arr[0..i-1], тобто
        # більше ключа key, на одну позицію вперед їхньої поточної позиції
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr
