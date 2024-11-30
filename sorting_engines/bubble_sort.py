"""
Бульбашковий алгоритм сортування

Time Complexity: O(n^2)
Auxiliary Space: O(1)
"""
from busy_time_meter import busy_time_meter


@busy_time_meter
# Функція бульбашкового сортування
def bubble_sort(arr):
    n = len(arr)
    # Пройти по всіх елементах масиву
    for i in range(n):
 
        # Останній та i-й елементи вже на місці
        for j in range(0, n-i-1):

            # Обхід масиву від 0 до n-i-1
            # Поміняти місцями, якщо знайдений елемент більший ніж наступний елемент
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
