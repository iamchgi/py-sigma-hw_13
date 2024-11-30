"""
Сортування злиттям
Time Complexity: O(n log(n))
Auxiliary Space: O(n)
"""
from busy_time_meter import busy_time_meter

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Ділимо масиви на дві частини
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Злиття двох відвпорядкованих половин
    return merge(left_half, right_half)

def merge(left, right):
    sorted_array = []
    i = j = 0

    # Порівнюєм елементи і поєднуєм масиви
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Додоєм елементи що залишилися
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array

@busy_time_meter
def merge_sort_array(arr):
    return merge_sort(arr)