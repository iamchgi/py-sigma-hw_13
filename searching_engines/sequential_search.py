"""
Послідовний (лінійний) пошук - sequential (linear) search:
Time Complexity: O(n)
Auxiliary Space: O(1) for iterative and O(n) for recursive.
застосовується для невеликих масивів даних.

"""
from busy_time_meter import busy_time_meter

@busy_time_meter
def linear_search_one_element(key, arr):
    n = len(arr)
    key_position = -1
    for i in range(n):
        if (arr[i] == key):
            key_position = i
#            return key_position
            # print("The element is found at position", key_position)
    # if (key_position == 0):
    #     print("The element is not present in the array")
    return key_position

@busy_time_meter
def linear_search_many_elements(key, arr):
    arr_key_position = []
    n = len(arr)
    key_position = 0
    for i in range(n):
        if (arr[i] == key):
            key_position = i
            arr_key_position.append(key_position)
    # if (key_position == 0):
    #     print("The element is not present in the array")
    return arr_key_position
